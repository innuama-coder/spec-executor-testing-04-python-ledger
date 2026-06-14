import unittest

from src.ledger_totals import calculate_invoice_total


class LedgerTotalsTest(unittest.TestCase):
    def test_empty_invoice(self):
        self.assertEqual(
            calculate_invoice_total([]),
            {"subtotal": 0.0, "discount": 0.0, "tax": 0.0, "total": 0.0},
        )


if __name__ == "__main__":
    unittest.main()

