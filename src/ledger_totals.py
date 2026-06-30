"""Invoice total helpers."""

from decimal import Decimal, ROUND_HALF_UP


_CENT = Decimal("0.01")


def _as_decimal(value):
    return Decimal(str(value))


def _round_money(value):
    return float(value.quantize(_CENT, rounding=ROUND_HALF_UP))


def calculate_invoice_total(items, discount_rate=0, tax_rate=0):
    """Calculate subtotal, discount, tax, and total for invoice line items."""
    discount_rate = _as_decimal(discount_rate)
    tax_rate = _as_decimal(tax_rate)

    if discount_rate < 0:
        raise ValueError("discount_rate cannot be negative")
    if tax_rate < 0:
        raise ValueError("tax_rate cannot be negative")

    subtotal = Decimal("0")
    for item in items:
        quantity = _as_decimal(item["quantity"])
        unit_price = _as_decimal(item["unit_price"])

        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        if unit_price < 0:
            raise ValueError("unit_price cannot be negative")

        subtotal += quantity * unit_price

    discount = subtotal * discount_rate
    tax = (subtotal - discount) * tax_rate
    total = subtotal - discount + tax

    return {
        "subtotal": _round_money(subtotal),
        "discount": _round_money(discount),
        "tax": _round_money(tax),
        "total": _round_money(total),
    }
