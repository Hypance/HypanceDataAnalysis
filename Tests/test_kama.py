import unittest
import pandas as pd
import numpy as np
from hyta.kama import KAMA

class TestKAMA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_excel("files/kama.xlsx")

    def setUp(self):
        self.ind = KAMA(self.df["Close"],10,2,30) 

    def tearDown(self):
        del self.ind

    @classmethod
    def tearDownClass(cls):
        del cls.df

    def test_change(self): 
        pd.testing.assert_series_equal(self.df["change"],self.ind.change(),check_names=False)
        self.assertIsInstance(self.ind.change(),pd.Series)
        self.assertEqual(np.isnan(self.ind.change()[9]),True)

    def test_volatility(self):
        pd.testing.assert_series_equal(self.df["volatility"],self.ind.volatility(),check_names=False)
        self.assertIsInstance(self.ind.volatility(),pd.Series)
        self.assertEqual(np.isnan(self.ind.volatility()[0]),True)

    def test_efficiency_ratio(self):
        pd.testing.assert_series_equal(self.df["ER"],self.ind.efficiency_ratio(),check_names=False,check_series_type=True)
        self.assertIsInstance(self.ind.efficiency_ratio(),pd.Series)
        self.assertEqual(np.isnan(self.ind.efficiency_ratio()[9]),True)       
    
    def test_smoothing_constant(self):
        self.assertAlmostEqual(self.df["SC"].any(),self.ind.smoothing_constant().any(),4)
        self.assertIsInstance(self.ind.smoothing_constant(),pd.Series)
        self.assertEqual(np.isnan(self.ind.smoothing_constant()[9]),True)

    def test_kama(self):
        pd.testing.assert_series_equal(self.df["KAMA"],self.ind.calc_kama(),check_names=False)
        self.assertIsInstance(self.ind.calc_kama(),pd.Series)
        self.assertEqual(np.isnan(self.ind.calc_kama()[8]),True)
        self.assertEqual(self.ind.calc_kama()[9],self.df["Close"][9])

if __name__ == "__main__":
    unittest.main()