"""Prices are integer cents."""


def apply_discount(price_cents: int, percent: int) -> int:
    """Take `percent` off a price."""
    return price_cents - price_cents * percent // 100
