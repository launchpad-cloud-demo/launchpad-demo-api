"""Prices are integer cents."""


def apply_discount(price_cents: int, percent: int) -> int:
    """Take `percent` off a price, rounding the discount to the nearest cent."""
    return price_cents - (price_cents * percent + 50) // 100
