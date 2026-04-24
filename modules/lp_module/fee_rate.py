from dataclasses import dataclass
from typing import Optional


@dataclass
class FeeRateSnapshot:
    fees_usd: float
    raw_rate_usd_per_min: Optional[float]
    ema_rate_usd_per_min: Optional[float]
    window_span_sec: float
    samples: int


class FeeRateTracker:
    def __init__(self, window_sec: float = 1800.0, alpha: float = 0.4) -> None: ...
    def reset(self) -> None: ...
    def warm_from_history(self, samples: list, seed_ema: Optional[float] = None) -> int: ...
    def update(self, fees_usd: float, now_sec: Optional[float] = None) -> FeeRateSnapshot: ...
