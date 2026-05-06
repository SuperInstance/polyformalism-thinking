```python
from dataclasses import dataclass
from typing import Optional, Literal


@dataclass
class IndemnificationClause:
    """
    Reconstructed verbatim from 7-channel A2A encoding.
    No extrapolation, no invented wording. All properties preserved exactly.
    """

    # ==============================================
    # C1 [BOUNDARY] | CLARITY 4
    # ==============================================
    claim_scope: Literal["Only breach of Section 4.2 representations/warranties"]
    maximum_cap: Literal["Full aggregate consideration paid under agreement"]
    has_carveouts: bool = False
    has_time_limits: bool = False
    has_claim_type_exceptions: bool = False

    # ==============================================
    # C2 [PATTERN] | CLARITY 5
    # ==============================================
    obligation_flow: Literal["Unidirectional: First Party -> Second Party only"]
    trigger_sequence: tuple[str, str, str] = ("qualifying_breach", "valid_claim", "capped_payment")
    grants_reciprocal_rights: bool = False

    # ==============================================
    # C3 [PROCESS] | CLARITY 2
    # ==============================================
    defines_procedural_steps: bool = False
    specifies_claim_notification_timing: bool = False
    specifies_breach_verification_rules: bool = False
    specifies_dispute_escalation: bool = False
    specifies_payment_timelines: bool = False
    only_defines_final_liability_bounds: bool = True

    # ==============================================
    # C4 [KNOWLEDGE] | CLARITY 4
    # ==============================================
    is_contractually_binding: bool = True
    claim_evidence_requirement: Literal["External verifiable proof of breach + damages"]
    defined_standard_of_proof: Optional[None] = None

    # ==============================================
    # C5 [SOCIAL] | CLARITY 3
    # ==============================================
    risk_allocation: Literal["Asymmetric: First Party accepts 100% downside for this risk"]
    reflects_relative_negotiating_leverage: bool = True
    has_formal_dispute_authority_hierarchy: bool = False

    # ==============================================
    # C6 [DEEP] | CLARITY 3
    # ==============================================
    surface_expression: Literal["Formal legal promise to indemnify Second Party"]
    root_intent: tuple[str, str] = (
        "Cap maximum possible financial downside for First Party",
        "Provide Second Party with predictable bounded recourse"
    )
    design_goal: Literal["Balance risk exposure for both counterparties"]

    # ==============================================
    # C7 [INSTRUMENT] | CLARITY 1
    # ==============================================
    defines_execution_procedures: bool = False
    defines_claim_valuation_rules: bool = False
    defines_dispute_resolution_mechanisms: bool = False
    defines_alternate_remedies: bool = False
    only_specifies_maximum_indemnification_value: bool = True
```