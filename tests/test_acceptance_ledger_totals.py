import unittest

from src.ledger_totals import calculate_invoice_total


class LedgerTotalsAcceptanceTest(unittest.TestCase):
    def test_discount_and_tax_formula(self):
        result = calculate_invoice_total(
            [
                {"name": "analysis", "quantity": 2, "unit_price": 50},
                {"name": "support", "quantity": 1, "unit_price": 25},
            ],
            discount_rate=0.10,
            tax_rate=0.08,
        )
        self.assertEqual(
            result,
            {"subtotal": 125.0, "discount": 12.5, "tax": 9.0, "total": 121.5},
        )

    def test_rejects_negative_inputs(self):
        invalid_cases = [
            ([{"name": "bad", "quantity": -1, "unit_price": 10}], 0, 0),
            ([{"name": "bad", "quantity": 1, "unit_price": -10}], 0, 0),
            ([{"name": "bad", "quantity": 1, "unit_price": 10}], -0.1, 0),
            ([{"name": "bad", "quantity": 1, "unit_price": 10}], 0, -0.1),
        ]
        for items, discount_rate, tax_rate in invalid_cases:
            with self.subTest(items=items, discount_rate=discount_rate, tax_rate=tax_rate):
                with self.assertRaises(ValueError):
                    calculate_invoice_total(items, discount_rate, tax_rate)


if __name__ == "__main__":
    unittest.main()
