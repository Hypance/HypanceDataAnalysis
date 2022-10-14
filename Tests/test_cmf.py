import unittest
from hyta import CMF 
import pandas as pd
import numpy as np

class TestCmf(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel('cs-cmf.xls')
    
    @classmethod
    def tearDownClass(cls):
        del cls.data
    
    def setUp(self) -> None:
        self.close = self.data["Close"]
        self.low = self.data["Low"]
        self.high = self.data["High"]
        self.volume = self.data["Volume"]

        b = CMF(self.close,self.low,self.high,self.volume)
        self.mfm_result = b.money_flow_multiplier(self.close,self.low,self.high)
        self.mfv_result = b.money_flow_volume(self.mfm_result,self.volume)

    def test_mfm(self):
        self.assertAlmostEqual(self.mfm_result[1],self.data["MF Multiplier"][1])
        self.assertNotEqual(self.mfm_result[1],0.82323)
        self.assertIsNotNone(self.mfm_result[1])

    def test_mfv(self):
        self.assertAlmostEqual(self.mfv_result[1],self.data["MF Volume"][1])
        self.assertNotEqual(self.mfv_result[1],0.23000)
        self.assertIsNotNone(self.mfv_result[1])

    def test_cmf(self):
        a = CMF(self.close,self.low,self.high,self.volume)
        cmf_result = a.cmf()
        #self.assertEqual(type(cmf_result[1]),np.nan)
        self.assertIsInstance(cmf_result,pd.Series)
        np.testing.assert_equal(cmf_result[1],np.nan)
        self.assertGreater(cmf_result[23],-1)
        self.assertLess(cmf_result[23],1)

if __name__ == "__main__":
    unittest.main()