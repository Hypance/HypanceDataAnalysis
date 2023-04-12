import pandas as pd
from hyta.dema import DEMA
import unittest


class TestDema(unittest.TestCase):
    """
    In these tests, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(pandas series)
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/dema.xlsx")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    def test_ema1(self):
        original_ema = pd.Series(self.df["ema"])
        test_ema = DEMA(self.df["close"]).ema()
        self.assertAlmostEqual(original_ema[150], test_ema[150], places=7)
        self.assertAlmostEqual(original_ema.iloc[-1], test_ema.iloc[-1], places=7)
        self.assertEqual(len(original_ema), len(test_ema))
        self.assertIsInstance(test_ema, pd.Series)

    def test_ema2(self):
        original_dema = pd.Series(self.df["dema"])
        test_dema = DEMA(self.df["close"]).dema()
        self.assertAlmostEqual(original_dema[100], test_dema[100], places=7)
        self.assertAlmostEqual(original_dema.iloc[-1], test_dema.iloc[-1], places=6)
        self.assertEqual(len(original_dema), len(test_dema))
        self.assertIsInstance(test_dema, pd.Series)

    if __name__ == "__main__":
        unittest.main()
