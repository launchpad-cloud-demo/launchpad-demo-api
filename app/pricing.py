"""Prices are integer cents."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Discount:
    percent: int
    code: str


def apply_discount(price_cents: int, discount: Discount) -> int:
    """Take the discount off a price, rounding the discount to the nearest cent."""
    return price_cents - (price_cents * discount.percent + 50) // 100
