import pandas as pd
from hyta.aroon import Aroon
import unittest


class TestAroon(unittest.TestCase):
    """
    In this class, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(pandas series)
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/Aroon.Oscillator.xls")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    def test_aroon_up(self):
        original_aroon_up = pd.Series(self.df["Aroon Up"])
        test_aroon_up = Aroon(self.df["Adj Close"]).aroon_up()

        self.assertAlmostEqual(original_aroon_up[26], test_aroon_up[25])

        self.assertEqual(len(original_aroon_up), len(test_aroon_up))

        self.assertIsInstance(test_aroon_up, pd.Series)

    def test_aroon_down(self):
        original_aroon_down = pd.Series(self.df["Aroon Down"])
        test_aroon_down = Aroon(self.df["Adj Close"]).aroon_down()

        self.assertAlmostEqual(original_aroon_down[26], test_aroon_down[25])

        self.assertEqual(len(original_aroon_down), len(test_aroon_down))

        self.assertIsInstance(test_aroon_down, pd.Series)

    def test_aroon_oscilattor(self):
        original_aroon_oscilattor = pd.Series(self.df["Aroon Oscillator"])
        test_aroon_oscilattor = Aroon(self.df["Adj Close"]).aroon_oscilattor()

        self.assertAlmostEqual(original_aroon_oscilattor[26], test_aroon_oscilattor[25])

        self.assertEqual(len(original_aroon_oscilattor), len(test_aroon_oscilattor))

        self.assertIsInstance(test_aroon_oscilattor, pd.Series)

    if __name__ == "__main__":
        unittest.main()
