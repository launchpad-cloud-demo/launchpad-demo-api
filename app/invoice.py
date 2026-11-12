from app.pricing import Discount, apply_discount


def invoice_total(items: list[int], discount_percent: int) -> int:
    subtotal = sum(items)
    return apply_discount(subtotal, Discount(discount_percent, ""))


def label(total_cents: int) -> str:
    return f"${total_cents // 100}.{total_cents % 100:02d}"
