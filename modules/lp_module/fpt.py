from dataclasses import dataclass
from typing import Optional


@dataclass
class FPTSnapshot:
    e_t_remaining_min: Optional[float]
    log_dist_upper: float
    log_dist_lower: float
    sigma_per_minute: Optional[float]
    in_range: bool
    clamped: bool


def expected_time_in_range(
    current_price: float,
    lower: float,
    upper: float,
    sigma_per_minute: Optional[float],
) -> FPTSnapshot: ...
