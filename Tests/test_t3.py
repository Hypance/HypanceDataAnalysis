import pandas as pd
from hyta.t3tillson import t3Tillson
import unittest


class TestT3Tillson(unittest.TestCase):
    """
    In these tests, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(pandas series)
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/t3tillson.xlsx")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    def test_ema1(self):
        original_ema1 = pd.Series(self.df["ema1"])
        test_ema1 = t3Tillson(self.df["close"]).ema1()

        self.assertAlmostEqual(original_ema1[8], test_ema1[8], places=7)

        self.assertAlmostEqual(original_ema1.iloc[-1], test_ema1.iloc[-1], places=7)

        self.assertEqual(len(original_ema1), len(test_ema1))

        self.assertIsInstance(test_ema1, pd.Series)

    def test_ema2(self):
        original_ema2 = pd.Series(self.df["ema2"])
        test_ema2 = t3Tillson(self.df["close"]).ema2()

        self.assertAlmostEqual(original_ema2[10], test_ema2[10], places=7)

        self.assertAlmostEqual(original_ema2.iloc[-1], test_ema2.iloc[-1], places=7)

        self.assertEqual(len(original_ema2), len(test_ema2))

        self.assertIsInstance(test_ema2, pd.Series)

    def test_ema3(self):
        original_ema3 = pd.Series(self.df["ema3"])
        test_ema3 = t3Tillson(self.df["close"]).ema3()

        self.assertAlmostEqual(original_ema3[40], test_ema3[40], places=7)

        self.assertAlmostEqual(original_ema3.iloc[-1], test_ema3.iloc[-1], places=7)

        self.assertEqual(len(original_ema3), len(test_ema3))

        self.assertIsInstance(test_ema3, pd.Series)

    def test_ema4(self):
        original_ema4 = pd.Series(self.df["ema4"])
        test_ema4 = t3Tillson(self.df["close"]).ema4()

        self.assertAlmostEqual(original_ema4[29], test_ema4[29], places=7)

        self.assertAlmostEqual(original_ema4.iloc[-1], test_ema4.iloc[-1], places=7)

        self.assertEqual(len(original_ema4), len(test_ema4))

        self.assertIsInstance(test_ema4, pd.Series)

    def test_ema5(self):
        original_ema5 = pd.Series(self.df["ema5"])
        test_ema5 = t3Tillson(self.df["close"]).ema5()

        self.assertAlmostEqual(original_ema5[8], test_ema5[8], places=7)

        self.assertAlmostEqual(original_ema5.iloc[-1], test_ema5.iloc[-1], places=7)

        self.assertEqual(len(original_ema5), len(test_ema5))

        self.assertIsInstance(test_ema5, pd.Series)

    def test_ema6(self):
        original_ema6 = pd.Series(self.df["ema6"])
        test_ema6 = t3Tillson(self.df["close"]).ema6()

        self.assertAlmostEqual(original_ema6[17], test_ema6[17], places=5)

        self.assertAlmostEqual(original_ema6.iloc[-1], test_ema6.iloc[-1], places=7)

        self.assertEqual(len(original_ema6), len(test_ema6))

        self.assertIsInstance(test_ema6, pd.Series)

    def test_T3(self):
        originalT3 = pd.Series(self.df["t3"])

        testT3 = t3Tillson(self.df["close"]).T3()

        self.assertAlmostEqual(originalT3[15], testT3[15], places=7)

        self.assertAlmostEqual(originalT3.iloc[-1], testT3.iloc[-1], places=7)

        self.assertEqual(len(originalT3), len(testT3))

        self.assertIsInstance(testT3, pd.Series)

    if __name__ == "__main__":
        unittest.main()
