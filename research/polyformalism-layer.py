import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import MultiheadAttention
from typing import Optional, List

# Fallback for S4 if not installed
try:
    from s4 import S4
except ImportError:
    print("Warning: S4 not installed, using LSTM fallback for sequential head")
    class FallbackS4(nn.Module):
        def __init__(self, d_model: int):
            super().__init__()
            self.lstm = nn.LSTM(input_size=d_model, hidden_size=d_model, batch_first=True, bidirectional=False)
        def forward(self, x: torch.Tensor) -> torch.Tensor:
            return self.lstm(x)[0]
    S4 = FallbackS4

# Fallback for GNN if not installed
try:
    from torch_geometric.nn import GCNConv
except ImportError:
    print("Warning: torch_geometric not installed, using attention fallback for structural head")
    class FallbackGNN(nn.Module):
        def __init__(self, in_channels: int):
            super().__init__()
            self.attn = MultiheadAttention(embed_dim=in_channels, num_heads=8, batch_first=True, dropout=0.1)
            self.norm = nn.LayerNorm(in_channels)
            self.dropout = nn.Dropout(0.1)
        def forward(self, x: torch.Tensor) -> torch.Tensor:
            attn_out, _ = self.attn(x, x, x)
            attn_out = self.dropout(attn_out)
            return self.norm(x + attn_out)
    GCNConv = FallbackGNN

class PolyformalismLayer(nn.Module):
    def __init__(
        self,
        dim: int,
        num_heads: int = 4,
        attention_num_heads: int = 8,
        vocab_size: Optional[int] = None,
        lambda_diversity: float = 0.1,
        lambda_load_balance: float = 0.01
    ):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.lambda_diversity = lambda_diversity
        self.lambda_load_balance = lambda_load_balance

        # Head 0: Imperative thinking (Linear + ReLU)
        self.head0_linear = nn.Linear(dim, dim)

        # Head 1: Relational thinking (Attention-only self-attention)
        self.head1_attn = MultiheadAttention(
            embed_dim=dim,
            num_heads=attention_num_heads,
            batch_first=True,
            dropout=0.1
        )
        self.head1_norm = nn.LayerNorm(dim)
        self.head1_dropout = nn.Dropout(0.1)

        # Head 2: Sequential/temporal thinking (S4)
        self.head2_s4 = S4(d_model=dim)

        # Head3: Structural/topological thinking (GCN)
        self.head3_gnn = GCNConv(in_channels=dim, out_channels=dim) if not isinstance(GCNConv, FallbackGNN) else FallbackGNN(dim)

        # Gating mechanism: select heads per token
        self.gate_proj = nn.Linear(dim, num_heads)

        # Insight detector: compare head outputs for divergences
        self.insight_detector = nn.Sequential(
            nn.Linear(num_heads * dim, dim * 2),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(dim * 2, 1)
        )

        # Convergence layer: merge gated insights
        self.convergence_proj = nn.Sequential(
            nn.Linear(dim + 1, dim * 2),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(dim * 2, dim)
        )

        # LM head for language modeling loss
        self.vocab_size = vocab_size
        if vocab_size is not None:
            self.lm_head = nn.Linear(dim, vocab_size)

    def forward_head0(self, x: torch.Tensor) -> torch.Tensor:
        """Imperative thinking head: Linear + ReLU"""
        return F.relu(self.head0_linear(x))

    def forward_head1(self, x: torch.Tensor) -> torch.Tensor:
        """Relational thinking head: Self-attention only"""
        attn_output, _ = self.head1_attn(x, x, x)
        attn_output = self.head1_dropout(attn_output)
        return self.head1_norm(x + attn_output)

    def forward_head2(self, x: torch.Tensor) -> torch.Tensor:
        """Sequential thinking head: S4 state-space model"""
        return self.head2_s4(x)

    def forward_head3(self, x: torch.Tensor) -> torch.Tensor:
        """Structural thinking head: GCN over token graph"""
        B, S, _ = x.shape
        x_nodes = x.view(B * S, self.dim)

        if isinstance(self.head3_gnn, FallbackGNN):
            return self.head3_gnn(x)

        # Create edge index for adjacent tokens in each batch sequence
        edge_index = []
        for batch_idx in range(B):
            base = batch_idx * S
            for j in range(S - 1):
                edge_index.append([base + j, base + j + 1])
                edge_index.append([base + j + 1, base + j])

        edge_index = torch.tensor(edge_index, dtype=torch.long, device=x.device).t().contiguous()
        x_out = self.head3_gnn(x_nodes, edge_index)
        return x_out.view(B, S, self.dim)

    def forward(
        self,
        x: torch.Tensor,
        targets: Optional[torch.Tensor] = None
    ) -> tuple[torch.Tensor, Optional[torch.Tensor]]:
        """
        Forward pass of PolyformalismLayer
        Args:
            x: Input concept embedding of shape [batch, seq_len, dim]
            targets: Optional target tokens for LM loss of shape [batch, seq_len]
        Returns:
            final_output: Merged tensor of shape [batch, seq_len, dim]
            total_loss: Total training loss if targets are provided, else None
        """
        B, S, _ = x.shape

        # Compute outputs from all formalism heads
        h0 = self.forward_head0(x)
        h1 = self.forward_head1(x)
        h2 = self.forward_head2(x)
        h3 = self.forward_head3(x)
        head_outputs: List[torch.Tensor] = [h0, h1, h2, h3]

        # Gating mechanism: per-token head selection weights
        gate_logits = self.gate_proj(x)
        gate_weights = F.softmax(gate_logits, dim=-1)

        # Compute gated combined output
        gated_output = torch.zeros_like(x)
        for i in range(self.num_heads):
            gated_output += gate_weights[..., i].unsqueeze(-1) * head_outputs[i]

        # Compute insight scores: divergence across heads
        cat_heads = torch.cat(head_outputs, dim=-1)
        insight_scores = self.insight_detector(cat_heads)

        # Merge insights into final output
        concat_input = torch.cat([gated_output, insight_scores], dim=-1)
        final_output = self.convergence_proj(concat_input)

        total_loss = None
        if targets is not None and self.vocab_size is not None:
            # LM Loss
            lm_logits = self.lm_head(final_output)
            lm_loss = F.cross_entropy(lm_logits.view(-1, self.vocab_size), targets.view(-1))

            # Formalism Diversity Loss
            diversity_loss = 0.0
            pair_count = self.num_heads * (self.num_heads - 1) // 2
            for i in range(self.num_heads):
                for j in range(i + 1, self.num_heads):
                    hi_flat = head_outputs[i].view(B * S, self.dim)
                    hj_flat = head_outputs[j].view(B * S, self.dim)
                    cos_sim = F.cosine_similarity(hi_flat, hj_flat, dim=1)
                    diversity_loss += (1 - cos_sim.mean())
            diversity_loss /= pair_count

            # Load Balance Loss
            mean_gate_per_head = gate_weights.mean(dim=[0, 1])
            ideal_gate = torch.full_like(mean_gate_per_head, 1.0 / self.num_heads)
            load_balance_loss = F.mse_loss(mean_gate_per_head, ideal_gate)

            total_loss = lm_loss + self.lambda_diversity * diversity_loss + self.lambda_load_balance * load_balance_loss

        return final_output, total_loss

def test_polyformalism_layer()