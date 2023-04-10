import unittest
import numpy as np
import pandas as pd
from hyta.tma import TMA


class TestTriangularMovingAverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/TMA.xlsx")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    """
    In this module, testing the following things:
    MA can not be lower than 0.
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(np.ndarray)
    """

    def testFirstMA(self):
        originalMA = np.array(self.df["FirstMA"])[19:]
        testMA = TMA(np.array(self.df["close"])).ma()

        self.assertAlmostEqual(originalMA[10], testMA[10])

        self.assertAlmostEqual(originalMA[-1], testMA[-1], places=7)

        self.assertEqual(len(originalMA), len(testMA))

        self.assertGreaterEqual(np.nanmin(testMA), 0.0)

        self.assertIsInstance(testMA, np.ndarray)

    """
    In this module, testing the following things:
    MA can not be lower than 0.
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(np.ndarray)
    """

    def testTMA(self):
        originalTMA = np.array(self.df["TMA"])[38:]
        testTMA = TMA(np.array(self.df["close"])).tma()

        self.assertAlmostEqual(originalTMA[10], testTMA[10])

        self.assertAlmostEqual(originalTMA[-1], testTMA[-1], places=7)

        self.assertEqual(len(originalTMA), len(testTMA))

        self.assertGreaterEqual(np.nanmin(testTMA), 0.0)

        self.assertIsInstance(testTMA, np.ndarray)


if __name__ == "__main__":
    unittest.main()
