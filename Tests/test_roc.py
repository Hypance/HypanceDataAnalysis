import unittest
import pandas as pd 
import numpy as np
from hyta.roc import ROC

class TestRateOfChange(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/ROC.xlsx")
        cls.close = np.array(cls.df["close"])
    
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df
    
    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(np.ndarray)
    [12:] is necessary to skip the empty values of ROC in Sample Excel.
    '''


    def test_Roc(self):
        
        original = np.array(self.df["ROC"][12:])
        
        test = ROC(self.close).roc()
        
        self.assertIsNotNone(test)
                
        self.assertAlmostEqual(original[25],test[25])
        
        self.assertEqual(len(original),len(test)) 

        self.assertIsInstance(test,pd.Series)

 

if __name__ == "__main__":
    unittest.main()