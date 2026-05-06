```python
from typing import Set, FrozenSet

# ==============================================
# DOMAIN SCOPE: Applies ONLY to connected finite graphs
# No edge cases, disconnected or infinite graphs are addressed
# ==============================================

class ConnectedGraph:
    """
    Core graph properties for cycle basis foundations.
    All assertions below are stated as established proven results from graph theory.
    No proofs, citations, or uncertainty bounds are provided in this specification.
    """
    vertices: Set[int]
    edges: Set[FrozenSet[int]]

    def spanning_tree_size(self) -> int:
        """Fixed invariant linear relation: |T| = |V| - 1"""
        return len(self.vertices) - 1

    def cyclomatic_number(self) -> int:
        """Exact arithmetic relation for independent cycle count"""
        return len(self.edges) - len(self.vertices) + 1

    def inject_non_tree_edge(self, spanning_tree: Set[FrozenSet[int]], edge: FrozenSet[int]) -> None:
        """
        Only defined dynamic operation.
        Accepts only edges that exist in the graph but not the spanning tree.
        
        GUARANTEED BEHAVIOUR: Exactly one unique cycle will be created on every valid call.
        Each non-tree edge maps 1:1 to an independent basis cycle.

        No edge removal, operation sequences, or other dynamics are implemented.
        """
        if edge not in self.edges or edge in spanning_tree:
            raise ValueError("Only edges from E\\T are permitted")
        # Cycle formation is mathematically guaranteed here
        pass


# ==============================================
# IMPLICIT UNDERLYING PURPOSE
# ==============================================
# This is the foundational mathematical base for:
#   - Spanning tree decomposition
#   - Cycle basis construction
#   - Graph cycle counting
#   - Connectivity analysis algorithms
#
# No concrete algorithms, software tools, or alternative methods are defined.
# This is a pure technical specification with no social framing, hierarchy, urgency or author intent signals.
```

---
All 7 channel properties are preserved exactly as encoded:
1.  ✅ C1: Strict scope boundary, no out-of-domain handling
2.  ✅ C2: All invariant mathematical relations and 1:1 edge-cycle mapping
3.  ✅ C3: Only the single defined operation, explicit statement of unimplemented behaviour
4.  ✅ C4: Epistemic status marked as asserted proven fact, no justification included
5.  ✅ C5: Explicit confirmation of zero social dimension content
6.  ✅ C6: Unstated root purpose of cycle basis foundation documented
7.  ✅ C7: Instrumental use cases listed, with note that no concrete tools are provided