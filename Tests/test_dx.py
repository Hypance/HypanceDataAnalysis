import unittest
from hyta.dx import DX
import pandas as pd
import numpy as np

class testDX(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = pd.read_excel("Tests/files/cs-dx.xlsx")

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.data

    def setUp(self) -> None:
        self.high = self.data["High"]
        self.low = self.data["Low"]
        self.close = self.data["Close"]
        self.dx_data = DX(high=self.high,low=self.low,close=self.close)
        self.fix1_number = 2
        self.fix2_number = 23
    
    def test_plus_dm(self):
        self.plus_dm_result = self.dx_data.plus_dm()
        self.assertAlmostEqual(self.plus_dm_result[self.fix1_number], self.data["+DM 1"][self.fix1_number])
        self.assertIsNotNone(self.plus_dm_result[self.fix2_number])
        self.assertIsInstance(self.plus_dm_result,pd.Series)
        self.assertGreaterEqual(np.nanmin(self.plus_dm_result),0)
    
    def test_minus_dm(self):
        self.minus_dm_result = self.dx_data.minus_dm()
        self.assertAlmostEqual(self.minus_dm_result[self.fix1_number], self.data["-DM 1"][self.fix1_number])
        self.assertIsNotNone(self.minus_dm_result[self.fix2_number])
        self.assertIsInstance(self.minus_dm_result,pd.Series)
        self.assertGreaterEqual(np.nanmin(self.minus_dm_result),0)

    def test_smoothed_plus_dm14(self):
        self.smoothed_plus_dm14_result = self.dx_data.smoothed_plus_dm14()
        self.assertAlmostEqual(self.smoothed_plus_dm14_result[self.fix2_number],self.data["+DM14"][self.fix2_number])
        self.assertIsInstance(self.smoothed_plus_dm14_result,pd.Series)

    def test_smoothed_minus_dm14(self):
        self.test_smoothed_minus_dm14_result = self.dx_data.smoothed_minus_dm14()
        self.assertAlmostEqual(self.test_smoothed_minus_dm14_result[self.fix2_number],self.data["-DM14"][self.fix2_number])
        self.assertIsInstance(self.test_smoothed_minus_dm14_result,pd.Series)

    def test_smoothed_tr14(self):
        self.test_smoothed_tr14_result = self.dx_data.smoothed_tr14()
        self.assertAlmostEqual(self.test_smoothed_tr14_result[self.fix2_number], self.data["TR14"][self.fix2_number])
        self.assertIsInstance(self.test_smoothed_tr14_result,pd.Series)

    def test_plus_di_14(self):
        self.test_plus_di_14_result =  self.dx_data.plus_di_14()
        self.assertAlmostEqual(self.test_plus_di_14_result[self.fix2_number], self.data["+DI14"][self.fix2_number])
        self.assertIsInstance(self.test_plus_di_14_result,pd.Series)

    def test_minus_di_14(self):
        self.test_minus_di_14_result = self.dx_data.minus_di_14()
        self.assertAlmostEqual(self.test_minus_di_14_result[self.fix2_number], self.data["-DI14"][self.fix2_number])
        self.assertIsInstance(self.test_minus_di_14_result,pd.Series)

    def test_di_diff(self):
        self.test_di_diff_result = self.dx_data.di_diff()
        self.assertAlmostEqual(self.test_di_diff_result[self.fix2_number], self.data["DI 14 Diff"][self.fix2_number])
        self.assertIsInstance(self.test_di_diff_result,pd.Series)

    def test_di_sum(self):
        self.test_di_sum_result = self.dx_data.di_sum()
        self.assertAlmostEqual(self.test_di_sum_result[self.fix2_number], self.data["DI 14 Sum"][self.fix2_number])
        self.assertIsInstance(self.test_di_sum_result,pd.Series)
    
    def test_dx(self):
        self.test_dx_result = self.dx_data.dx()
        self.assertAlmostEqual(self.test_dx_result[self.fix2_number], self.data["DX"][self.fix2_number])
        self.assertIsInstance(self.test_dx_result,pd.Series)

if __name__ == "__main__":
    unittest.main()