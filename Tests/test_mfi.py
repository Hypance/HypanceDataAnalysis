import unittest
from hyta.mfi import MFI
import pandas as pd
import numpy as np


class TestCmf(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel("Tests/files/cs-mfi.xls")

    @classmethod
    def tearDownClass(cls):
        del cls.data

    def setUp(self) -> None:
        self.close = self.data["Close"]
        self.low = self.data["Low"]
        self.high = self.data["High"]
        self.volume = self.data["Volume*"]
        self.mfi_data = MFI(self.close, self.low, self.high, self.volume)

    def test_typical_price(self):
        self.typical_price = self.mfi_data.typical_price()
        self.assertAlmostEqual(self.typical_price[1], self.data["Typical Price"][1])
        self.assertAlmostEqual(self.typical_price[7], self.data["Typical Price"][7])
        self.assertIsInstance(self.typical_price, pd.Series)

    def test_raw_money_flow(self):
        self.raw_money_flow = self.mfi_data.raw_money_flow()
        self.assertAlmostEqual(self.raw_money_flow[1], self.data["Raw Money Flow"][1])
        self.assertAlmostEqual(self.raw_money_flow[12], self.data["Raw Money Flow"][12])
        self.assertNotEqual(self.raw_money_flow[13], 0.23000)
        self.assertIsNotNone(self.raw_money_flow[2])

    def test_up_or_down(self):
        self.up_or_down = self.mfi_data.up_or_down()
        self.assertIsInstance(self.up_or_down, list)
        self.assertIsNotNone(self.up_or_down[23])
        self.assertEqual(np.nanmin(self.up_or_down), -1.0)
        self.assertEqual(np.nanmax(self.up_or_down), 1.0)

    def test_one_period_positive_mf(self):
        self.one_period_positive_mf = self.mfi_data.one_period_positive_mf()
        self.assertIsInstance(self.one_period_positive_mf, pd.Series)
        self.assertAlmostEqual(
            self.one_period_positive_mf[2], self.data["1-period Positive Money Flow"][2]
        )

    def test_one_period_negative_mf(self):
        self.one_period_negative_mf = self.mfi_data.one_period_negative_mf()
        self.assertIsInstance(self.one_period_negative_mf, pd.Series)
        self.assertAlmostEqual(
            self.one_period_negative_mf[5], self.data["1-period Negative Money Flow"][5]
        )

    def test_positive_money_flow(self):
        self.positive_money_flow = self.mfi_data.positive_money_flow()
        self.assertIsInstance(self.positive_money_flow, pd.Series)
        self.assertAlmostEqual(
            self.positive_money_flow[19], self.data["14-period Positive Money Flow"][19]
        )

    def test_negative_money_flow(self):
        self.negative_money_flow = self.mfi_data.negative_money_flow()
        self.assertIsInstance(self.negative_money_flow, pd.Series)
        self.assertAlmostEqual(
            self.negative_money_flow[26], self.data["14-period Negative Money Flow"][26]
        )

    def test_money_ratio(self):
        self.money_ratio = self.mfi_data.money_ratio()
        self.assertAlmostEqual(
            self.money_ratio[23], self.data["14-period Money Flow Ratio"][23]
        )
        self.assertIsInstance(self.money_ratio, pd.Series)

    def test_money_flow_index(self):
        self.money_flow_index = self.mfi_data.money_flow_index()
        self.assertIsInstance(self.money_flow_index, pd.Series)
        self.assertGreater(np.nanmin(self.money_flow_index), 0)
        self.assertLess(np.nanmax(self.money_flow_index), 100)


if __name__ == "__main__":
    unittest.main()
