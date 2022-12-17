import unittest
from hyta.cmf import CMF 
import pandas as pd
import numpy as np

class TestCmf(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel('Tests/files/cs-cmf.xls')

    @classmethod
    def tearDownClass(cls):
        del cls.data

    def setUp(self) -> None:
        self.close = self.data["Close"]
        self.low = self.data["Low"]
        self.high = self.data["High"]
        self.volume = self.data["Volume"]
        self.cmf_data = CMF(self.close,self.low,self.high,self.volume)

    def test_mfm(self):
        self.mfm_result = self.cmf_data.money_flow_multiplier()
        self.assertIsNotNone(self.mfm_result[1])
        self.assertAlmostEqual(self.mfm_result[1],self.data["MF Multiplier"][1])
        self.assertAlmostEqual(self.mfm_result[3],self.data["MF Multiplier"][3])
        self.assertNotEqual(self.mfm_result[1],0.82323)

    def test_mfv(self):
        self.mfv_result = self.cmf_data.money_flow_volume()
        self.assertIsNotNone(self.mfv_result[1])
        self.assertAlmostEqual(self.mfv_result[1],self.data["MF Volume"][1])
        self.assertAlmostEqual(self.mfv_result[5],self.data["MF Volume"][5])
        self.assertNotEqual(self.mfv_result[1],0.23000)

    def test_cmf(self):
        self.cmf_result = self.cmf_data.cmf()
        self.assertIsInstance(self.cmf_result,pd.Series)
        np.testing.assert_equal(self.cmf_result[1],np.nan)
        self.assertGreater(np.nanmin(self.cmf_result),-1)
        self.assertLess(np.nanmax(self.cmf_result),1)

if __name__ == "__main__":
    unittest.main()

