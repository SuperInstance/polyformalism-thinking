```python
from dataclasses import dataclass
from typing import Final, Literal, Optional

@dataclass(frozen=True)  # Represents single immutable instantaneous snapshot
class IMUTelemetrySnapshot:
    """
    Reconstructed IMU telemetry message, decoded from 7-channel A2A representation.
    All observed properties and absent metadata are preserved exactly as signaled.
    """

    # Inertial axis ordering, units and baseline state per encoding:
    accel_x: float  # Unit: g, resting near 0 neutral
    accel_y: float  # Unit: g, resting near 0 neutral
    accel_z: float  # Unit: g, resting at 1.0 gravity baseline
    gyro_x: float   # Unit: °/s, resting near 0 neutral
    gyro_y: float   # Unit: °/s, resting near 0 neutral
    gyro_z: float   # Unit: °/s, resting near 0 neutral

    system_health: Literal["NOMINAL"]
    attitude_roll: float  # Unit: degrees, near level
    attitude_pitch: float # Unit: degrees, near level

    # Confirmed state properties extracted from all channels:
    IS_STATIONARY: Final[bool] = True
    ONLY_EXTREMELY_SLOW_ROTATION: Final[bool] = True
    NO_DYNAMIC_MOTION_EVENTS: Final[bool] = True
    NO_FAULT_CONDITIONS: Final[bool] = True
    IS_ROUTINE_PASSIVE_MONITORING: Final[bool] = True
    ACTION_REQUIRED: Final[bool] = False

    # Explicitly ABSENT information confirmed across channels:
    SAMPLING_RATE: Final[Optional[None]] = None
    TIME_HISTORY: Final[Optional[None]] = None
    FAULT_THRESHOLDS: Final[Optional[None]] = None
    MEASUREMENT_RANGE: Final[Optional[None]] = None
    CALIBRATION_STATUS: Final[Optional[None]] = None
    MEASUREMENT_UNCERTAINTY: Final[Optional[None]] = None
    SENSOR_MODEL: Final[Optional[None]] = None
    FILTERING_METHOD: Final[Optional[None]] = None

    def root_intent(self) -> str:
        """Unstated core message this telemetry was generated to communicate"""
        return "IMU is operating normally, stationary, holding near level attitude with no abnormal motion."
```

This reconstruction:
1.  Uses native Python idioms (immutable dataclass, type hints, Final constants)
2.  Preserves *every* stated fact including what data was **not present** in the original encoding
3.  Separates measured values, observed state, absent metadata and root intent exactly as mapped across the 7 channels
4.  Does not invent any unstated values or assumptions
5.  Retains all unit, ordering and baseline properties from the original encoding