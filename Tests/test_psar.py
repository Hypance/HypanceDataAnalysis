import unittest
import numpy as np
import pandas as pd
from hyta.psar import ParabolicSAR

class TestPSAR(unittest.TestCase):
    
    path="Tests/files/PSAR.xlsx"

    @classmethod
    def setUpClass(cls):
        cls.data=pd.read_excel(cls.path)
        cls.close = cls.data['Close'].to_list()
        cls.high = cls.data['High'].to_list()
        cls.low = cls.data['Low'].to_list()
        cls.result_psar=cls.data['PSAR'].to_list()

    @classmethod
    def tearDownClass(cls):
        del cls.data  
        del cls.close
        del cls.high
        del cls.low
        del cls.result_psar
        
    #below function is testing psar results with respect to excel spreadsheet      
    def test_psar(self):
        self.result = ParabolicSAR(self.high,self.low,self.close)
        self.assertEqual(round(self.result_psar[0],2), round(self.result.parabolic_sar()[0],2))
        self.assertEqual(round(self.result_psar[2],2), round(self.result.parabolic_sar()[2],2)) 
        self.assertEqual(round(self.result_psar[-1],2), round(self.result.parabolic_sar()[-1],2)) 
        self.assertEqual(len(self.result_psar), len(self.result.parabolic_sar()))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)