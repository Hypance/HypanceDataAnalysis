import pandas as pd 
import numpy as np 
import unittest 
from hyta.dpo import DPO

class Test_DetrendedPriceOscillator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("files/DPO.xlsx")    

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    '''
    In this module, testing the following things:
    Moving Average can not be lower than 0.
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(np.ndarray)
    '''

    def test_dpo_ma(self):
        
        original = np.array(self.df["MA-DPO"][19:])
        
        test = DPO(list(self.df['close']),20).moving_average()
                
        self.assertAlmostEqual(original[-1],test[-1]) 
        
        self.assertGreaterEqual(np.nanmin(test),0)  
        
        self.assertEqual(len(original),len(test)) 

        self.assertIsInstance(test,np.ndarray)

    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(np.ndarray)
    '''

    def test_closes(self):
        original = np.array(self.df["CLOSES-DPO"][19:])
        
        test = DPO(list(self.df['close']),20).closes()
                
        self.assertAlmostEqual(original[-1],test[-1]) 
        
        self.assertEqual(len(original),len(test)) 

        self.assertIsInstance(test,np.ndarray) 

    '''
    In this module, testing the following things:
    Element values are equal and is in the same index.
    Returns the same length data comparing to original data
    Returning list is same type as we want(np.ndarray)
    '''

    def test_dpo(self):
        original = np.array(self.df["DPO"][19:])
        
        test = DPO(list(self.df['close']),20).dpo()
                
        self.assertAlmostEqual(original[-1],test[-1]) 
        
        self.assertEqual(len(original),len(test)) # Testing output arrays element counts.

        self.assertIsInstance(test,np.ndarray)

if __name__ == "__main__":
    unittest.main()