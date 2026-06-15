```python
from typing import Optional, Literal
from dataclasses import dataclass
from enum import Enum

Clarity = Literal[1, 2, 3, 4]

class ActorType(Enum):
    CIVILIAN = "civilian"
    LAND_FORCES = "land_forces"
    NAVAL_FORCES = "naval_forces"
    MILITIA = "militia"

@dataclass
class OperationalContext:
    active_war: bool
    active_public_danger: bool
    actor_on_active_service: bool

class GrandJuryProtectionRule:
    """
    Reconstructed 1:1 intent from 7-channel A2A encoding.
    No external assumptions added. All encoded properties are preserved.
    """

    # Encoded channel clarity metadata
    channel_clarity: dict[str, Clarity] = {
        "boundary": 4,
        "pattern": 4,
        "process": 3,
        "knowledge": 2,
        "social": 4,
        "deep": 3,
        "instrument": 4
    }

    # ---------------- C1 [BOUNDARY] ----------------
    PROTECTED_OFFENSE_CATEGORIES = {"capital", "infamous"}
    BOUNDARY_AMBIGUOUS_TERMS = {"infamous crime"}
    PERFECT_SCOPE_CLARITY = False

    # ---------------- C2 [PATTERN] ----------------
    NO_CIVILIAN_EXCEPTION_PATHS = True
    EXCEPTION_IS_OVERRIDING_GATE = True
    EXCEPTION_REQUIRES_ALL_CONDITIONS_MET = True

    # ---------------- C3 [PROCESS] ----------------
    MANDATORY_EXECUTION_ORDER = ("grand_jury_action", "hold_person_to_answer")
    EXCEPTION_ONLY_ACTIVE_DURING_SERVICE = True
    EXCEPTION_NOT_RETROACTIVE = True
    UNSPECIFIED_PROCESS_DETAILS = [
        "grand_jury_timelines",
        "grand_jury_deliberation_standards",
        "grand_jury_procedure_rules"
    ]

    # ---------------- C4 [KNOWLEDGE] ----------------
    IS_BINDING_CONSTITUTIONAL_LAW = True
    NO_JUSTIFICATION_OR_EVIDENCE_PROVIDED = True
    UNDEFINED_LEGAL_TERMS = {"infamous crime", "public danger"}
    IS_PRESCRIPTIVE_NOT_EXPLANATORY = True

    # ---------------- C5 [SOCIAL] ----------------
    PRIMARY_FUNCTION = "constrain state prosecutorial power"
    REQUIRES_INDEPENDENT_CIVILIAN_AUTHORIZATION = True
    MILITARY_AUTHORITY_SUPERSEDES_DURING_EMERGENCY = True
    FORMALIZES_CIVIL_MILITARY_POWER_HIERARCHY = True

    # ---------------- C6 [DEEP] ----------------
    SURFACE_SEMANTICS = "neutral procedural charging requirement"
    UNSTATED_ROOT_INTENT = "prevent arbitrary unaccountable state prosecution of serious offenses"
    EMBEDDED_UNACKNOWLEDGED_TENSION = "individual liberty vs emergency state power"

    # ---------------- C7 [INSTRUMENT] ----------------
    AUTHORIZED_CHARGING_MECHANISMS = {"grand_jury_presentment", "grand_jury_indictment"}
    NO_ALTERNATIVE_CIVILIAN_CHARGING_PERMITTED = True
    NO_PROHIBITED_PROCEDURES_EXPLICITLY_LISTED = True


    def can_initiate_charges(self, actor: ActorType, offense_type: str, context: OperationalContext) -> tuple[bool, Optional[str]]:
        """Core encoded rule logic, no interpretation added"""

        # Bypass rule entirely for out-of-scope offenses
        if offense_type not in self.PROTECTED_OFFENSE_CATEGORIES:
            return True, "Offense outside protection boundary"

        # Military exception gate evaluated first per encoding
        if (
            actor in {ActorType.LAND_FORCES, ActorType.NAVAL_FORCES, ActorType.MILITIA}
            and context.actor_on_active_service
            and (context.active_war or context.active_public_danger)
        ):
            return True, "Active emergency military service exception applies"

        # Default rule for all other cases
        return False, "Mandatory prerequisite: Grand Jury presentment or indictment required"
```