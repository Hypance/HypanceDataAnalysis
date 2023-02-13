import unittest
import pandas as pd

from hyta.hma import HullMovingAverage


class TestHullMovingAverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = pd.read_excel("Tests/files/HMA.xlsx")
        cls.close = cls.data["CLOSE"].to_list()
        cls.hma = cls.data["HMA"].to_list()

    @classmethod
    def tearDownClass(cls):
        del cls.data
        del cls.close
        del cls.hma

    def test_hma(self):
        # period is 20 in this test.
        hma = HullMovingAverage(self.close, 20).hull_moving_average()
        self.assertAlmostEqual(hma, self.hma[0])
        self.assertIsInstance(hma, float)
        self.assertIsNotNone(hma)
