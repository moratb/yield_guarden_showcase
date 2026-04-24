from dataclasses import dataclass


@dataclass
class ILSnapshot:
    il_current_usd: float
    il_remaining_usd: float
    delta_price_pct: float
    half_range_pct: float
    total_position_usd: float
    il_at_edge_usd: float


def il_current_usd(
    entry_price: float,
    current_price: float,
    half_range_pct: float,
    total_position_usd: float,
) -> float: ...


def il_snapshot(
    entry_price: float,
    current_price: float,
    range_lower: float,
    range_upper: float,
    total_position_usd: float,
    il_at_edge_usd: float,
) -> ILSnapshot: ...
