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
        original_ema1 = pd.Series(self.df["ema1 t3"])
        test_ema1 = t3Tillson(self.df["close"]).ema1()

        self.assertAlmostEqual(original_ema1[100], test_ema1[100])

        self.assertAlmostEqual(original_ema1.iloc[-1], test_ema1.iloc[-1], places=7)

        self.assertEqual(len(original_ema1), len(test_ema1))

        self.assertIsInstance(test_ema1, pd.Series)

    def test_ema2(self):
        original_ema2 = pd.Series(self.df["ema2 t3"])
        test_ema2 = t3Tillson(self.df["ema1 t3"]).ema2()

        self.assertAlmostEqual(original_ema2[100], test_ema2[100])

        self.assertAlmostEqual(original_ema2[-1], test_ema2[-1], places=7)

        self.assertEqual(len(original_ema2), len(test_ema2))

        self.assertIsInstance(test_ema2, pd.Series)

    def test_ema3(self):
        original_ema3 = pd.Series(self.df["ema3 t3"])
        test_ema3 = t3Tillson(self.df["ema2 t3"]).ema3()

        self.assertAlmostEqual(original_ema3[100], test_ema3[100])

        self.assertAlmostEqual(original_ema3[-1], test_ema3[-1], places=7)

        self.assertEqual(len(original_ema3), len(test_ema3))

        self.assertIsInstance(test_ema3, pd.Series)

    def test_ema4(self):
        original_ema4 = pd.Series(self.df["ema4 t3"])
        test_ema4 = t3Tillson(self.df["ema3 t3"]).ema4()

        self.assertAlmostEqual(original_ema4[100], test_ema4[100])

        self.assertAlmostEqual(original_ema4[-1], test_ema4[-1], places=7)

        self.assertEqual(len(original_ema4), len(test_ema4))

        self.assertIsInstance(test_ema4, pd.Series)

    def test_ema5(self):
        original_ema5 = pd.Series(self.df["ema5 t3"])
        test_ema5 = t3Tillson(self.df["ema4 t3"]).ema5()

        self.assertAlmostEqual(original_ema5[100], test_ema5[100])

        self.assertAlmostEqual(original_ema5[-1], test_ema5[-1], places=7)

        self.assertEqual(len(original_ema5), len(test_ema5))

        self.assertIsInstance(test_ema5, pd.Series)

    def test_ema6(self):
        original_ema6 = pd.Series(self.df["ema6 t3"])
        test_ema6 = t3Tillson(self.df["ema5 t3"]).ema6()

        self.assertAlmostEqual(original_ema6[100], test_ema6[100])

        self.assertAlmostEqual(original_ema6[-1], test_ema6[-1], places=7)

        self.assertEqual(len(original_ema6), len(test_ema6))

        self.assertIsInstance(test_ema6, pd.Series)

    def test_T3(self):
        original_t3 = pd.Series(self.df["ema1 t3"])
        test_t3 = t3Tillson(self.df["t3"]).T3()

        self.assertAlmostEqual(original_t3[100], test_t3[100])

        self.assertAlmostEqual(original_t3[-1], test_t3[-1], places=7)

        self.assertEqual(len(original_t3), len(test_t3))

        self.assertIsInstance(test_t3, pd.Series)

    if __name__ == "_main_":
        unittest.main()
