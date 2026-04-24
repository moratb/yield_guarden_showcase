from typing import Optional


class EWMAVolatilityEstimator:
    def __init__(
        self,
        source: str = 'ccxt',
        token_address: Optional[str] = None,
        exchange_name: Optional[str] = None,
        symbol: Optional[str] = None,
        resolution: str = "15m",
        lookback_bars: int = 192,
        lambda_: float = 0.94,
        min_refresh_sec: float = 600.0,
    ) -> None: ...

    @property
    def sigma_per_minute(self) -> Optional[float]: ...

    def reset(self) -> None: ...
    def get_sigma_per_minute(self, force: bool = False) -> Optional[float]: ...
