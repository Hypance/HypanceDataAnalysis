import unittest
import numpy as np
import pandas as pd
from hyta.atr import ATR

class TestAverageTrueRange(unittest.TestCase):
    
    path="files/ATR.xls"

    @classmethod
    def setUpClass(cls):
        cls.data=pd.read_excel(cls.path)
        cls.data_high = cls.data['High'].to_list()
        cls.data_low = cls.data['Low'].to_list()        
        cls.data_close = cls.data['Close'].to_list()
        cls.result_tr = cls.data['TR'].to_list()
        cls.result_atr = cls.data['ATR'].to_list()
        cls.data_all=np.array([cls.data_high,cls.data_low,cls.data_close])    
        
    @classmethod
    def tearDownClass(cls):
        del cls.data
        del cls.data_high
        del cls.data_low  
        del cls.data_close
        del cls.result_tr
        del cls.result_atr
        del cls.data_all   
    
    #below function is testing true range results with respect to excel spreadsheet    
    def test_tr(self):
        self.result = ATR(self.data_all)
        
        self.assertEqual(self.result_tr[0], self.result.true_range()[0])
        self.assertEqual(self.result_tr[2], self.result.true_range()[2])    
        self.assertEqual(round(self.result_tr[-1],2), round(self.result.true_range()[-1],2))
       
        self.assertEqual(len(self.result_tr), len(self.result.true_range()))
        
    #below function is testing average true range results with respect to excel spreadsheet           
    def test_atr(self):  
        self.result = ATR(self.data_all)
	self.true_value1=14

        self.assertEqual(round(self.result_atr[self.true_value1+1],2), round(self.result.average_true_range()[2],2))
        self.assertEqual(round(self.result_atr[2],2), round(self.result.average_true_range()[2],2))
        self.assertEqual(self.result_atr[-1], self.result.average_true_range()[-1])
   
        self.assertEqual(len(self.result_atr)-self.true_value1+1, len(self.result.average_true_range()))        
    
    #below function is testing corresponding tr and atr results
    def test_tr_atr(self):
        self.result = ATR(self.data_all)
        self.true_value1=14

        self.assertGreater(len(self.result.true_range()), len(self.result.average_true_range()))
        self.assertEqual(len(self.result.true_range())-len(self.result.average_true_range()),self.true_value1-1)  
    
    #below functions is testing for getting different true_value 
    def test_tr_atr_true_value_20(self):
        self.result_tr_20=ATR(self.data_all,20).true_range()
        self.result_atr_20=ATR(self.data_all,20).average_true_range()
        self.true_value2=20

        self.assertEqual(len(self.result_tr_20)-len(self.result_atr_20),self.true_value2-1) 
        
    def test_atr_none(self):
        self.result_atr_none=ATR(self.data_all,0).average_true_range()  

        np.testing.assert_equal(self.result_atr_none[-1],np.nan)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)