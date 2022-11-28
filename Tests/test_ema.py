import unittest
import pandas as pd
import numpy as np
from hyta.ema import EMA

class TestEma(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("files/ema.xlsx")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    def test_ema(self):
        ind = EMA(self.df["Close"],period=3)

        pd.testing.assert_series_equal(self.df["EMA"],ind.calc_ema(),check_names=False)
        self.assertEqual(len(self.df),len(ind.calc_ema().tolist()))
        self.assertIsInstance(ind.calc_ema(),pd.Series)
        self.assertEqual(np.isnan(ind.sma()[1]),True)     

if __name__ == "__main__":
    unittest.main()