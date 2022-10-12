import unittest
import numpy as np
import pandas as pd
from Test.ATR import ATR

class TestAverageTrueRange(unittest.TestCase):
    
    path=r"/Users/anilmehmetuyar/Downloads/ATR.xlsx"

    @classmethod
    def setUpClass(cls):
        cls.data=pd.read_excel(cls.path)
        cls.data_close = cls.data['Close'].to_list()
        cls.data_high = cls.data['High'].to_list()
        cls.data_low = cls.data['Low'].to_list()
        cls.data_all=np.array([cls.data_high,cls.data_low,cls.data_close])    
        
    @classmethod
    def tearDownClass(cls):
        del cls.data   
        
    def setUp(self):
        self.true_value1=14
        self.true_value2=20
        self.result00 = ATR(self.data_all)
        self.result01 = ATR(self.data_all,20)
        
        self.result1=ATR(self.data_all).TrueRange()
        self.result2=ATR(self.data_all).AverageTrueRange()
                
        self.result3=ATR(self.data_all,20).TrueRange()
        self.result4=ATR(self.data_all,20).AverageTrueRange()
        
        self.result5=ATR(self.data_all,0).AverageTrueRange()   
                
    def test_data(self):
        for i in range(len(self.data_all[2])):
            self.assertLess(abs(self.data_all[1][i]),abs(self.data_all[0][i]))
            self.assertLessEqual(abs(self.data_all[2][i]),abs(self.data_all[0][i]))
        
    def test_tr(self):        
        self.assertEqual(self.result1[0], self.result00.TrueRange()[0])
        self.assertEqual(self.result1[2], self.result00.TrueRange()[2])    
        self.assertEqual(self.result1[-1], self.result00.TrueRange()[-1])
        
        self.assertEqual(len(self.result1), len(self.result00.TrueRange()))
        
              
    def test_atr(self):        
        self.assertEqual(self.result2[0], self.result00.AverageTrueRange()[0])
        self.assertEqual(self.result2[2], self.result00.AverageTrueRange()[2])
        self.assertEqual(self.result2[-1], self.result00.AverageTrueRange()[-1])
   
        self.assertEqual(len(self.result2), len(self.result00.AverageTrueRange())) 
         
    
    def test_tr_atr(self):
        self.assertGreater(len(self.result00.TrueRange()), len(self.result00.AverageTrueRange())) 
        self.assertEqual(len(self.result00.TrueRange())-len(self.result00.AverageTrueRange()),self.true_value1-1)  

        
    def test_tr_atr_true_value_20(self):
        self.assertEqual(len(self.result3)-len(self.result4),self.true_value2-1) 
        
    def test_atr_none(self):
        np.testing.assert_equal(self.result5[-1],np.nan)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)