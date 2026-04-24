from dataclasses import dataclass
from typing import Optional


@dataclass
class EVSnapshot:
    fee_rate_usd_per_min: Optional[float]
    sigma_per_minute: Optional[float]
    e_t_remaining_min: Optional[float]
    il_current_usd: Optional[float]
    il_remaining_usd: Optional[float]
    ev_usd: Optional[float]
    ev_ema_usd: Optional[float]


def compute_ev_usd(
    fee_rate_usd_per_min: Optional[float],
    e_t_remaining_min: Optional[float],
    il_remaining_usd: Optional[float],
) -> Optional[float]: ...


def update_ev_ema(
    prev_ev_ema: Optional[float],
    ev_usd: Optional[float],
    alpha: float = 0.4,
) -> Optional[float]: ...
