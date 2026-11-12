from app.invoice import invoice_total, label
from app.pricing import Discount, apply_discount


def test_ten_percent_off() -> None:
    assert apply_discount(1999, Discount(10, "TEN")) == 1799


def test_invoice_total_with_discount() -> None:
    assert invoice_total([1999, 500], 15) == 2124


def test_label() -> None:
    assert label(2124) == "$21.24"
