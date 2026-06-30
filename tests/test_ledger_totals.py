import unittest

from src.ledger_totals import calculate_invoice_total


class LedgerTotalsTest(unittest.TestCase):
    def test_empty_invoice(self):
        self.assertEqual(
            calculate_invoice_total([]),
            {"subtotal": 0.0, "discount": 0.0, "tax": 0.0, "total": 0.0},
        )

    def test_single_line_item(self):
        self.assertEqual(
            calculate_invoice_total(
                [{"name": "consulting", "quantity": 3, "unit_price": 40}]
            ),
            {"subtotal": 120.0, "discount": 0.0, "tax": 0.0, "total": 120.0},
        )

    def test_multiple_line_items(self):
        self.assertEqual(
            calculate_invoice_total(
                [
                    {"name": "consulting", "quantity": 2, "unit_price": 75},
                    {"name": "hosting", "quantity": 4, "unit_price": 12.5},
                ]
            ),
            {"subtotal": 200.0, "discount": 0.0, "tax": 0.0, "total": 200.0},
        )

    def test_discount_and_tax_are_applied_in_order(self):
        self.assertEqual(
            calculate_invoice_total(
                [{"name": "implementation", "quantity": 5, "unit_price": 20}],
                discount_rate=0.10,
                tax_rate=0.05,
            ),
            {"subtotal": 100.0, "discount": 10.0, "tax": 4.5, "total": 94.5},
        )

    def test_amounts_are_rounded_to_two_decimal_places(self):
        self.assertEqual(
            calculate_invoice_total(
                [{"name": "usage", "quantity": 3, "unit_price": 0.333}],
                discount_rate=0.10,
                tax_rate=0.07,
            ),
            {"subtotal": 1.0, "discount": 0.1, "tax": 0.06, "total": 0.96},
        )

    def test_negative_inputs_raise_value_error(self):
        invalid_cases = [
            ([{"name": "bad quantity", "quantity": -1, "unit_price": 10}], 0, 0),
            ([{"name": "bad price", "quantity": 1, "unit_price": -10}], 0, 0),
            ([{"name": "bad discount", "quantity": 1, "unit_price": 10}], -0.01, 0),
            ([{"name": "bad tax", "quantity": 1, "unit_price": 10}], 0, -0.01),
        ]

        for items, discount_rate, tax_rate in invalid_cases:
            with self.subTest(items=items, discount_rate=discount_rate, tax_rate=tax_rate):
                with self.assertRaises(ValueError):
                    calculate_invoice_total(items, discount_rate, tax_rate)


if __name__ == "__main__":
    unittest.main()
