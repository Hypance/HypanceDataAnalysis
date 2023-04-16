import pandas as pd 
import numpy as np 
import unittest 
from hyta.uo import UO

class TestUltimateOscillator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/UO-datas.xlsx")
        cls.close = np.array(cls.df["close"])
        cls.high = np.array(cls.df["high"])
        cls.low = np.array(cls.df["low"])

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    

    def test_buyingPressure(self):
        '''
        In this module, testing the following things:
        Buying Pressure can not be negative number.
        Element values are equal and is in the same index.
        Returns the same length data comparing to original data
        Returning list is same type as we want(np.ndarray)
        '''
        
        original = np.array(self.df["BP-UO"][1:])
        
        test = UO(self.low,self.close,self.high).buyingPressure()
                
        self.assertAlmostEqual(original[25],test[25])
        
        self.assertGreaterEqual(np.nanmin(test),0)   
        
        self.assertEqual(len(original),len(test)) 

        self.assertIsInstance(test,np.ndarray)
    

    def test_trueRange(self):
        '''
        In this module, testing the following things:
        True Range can not be lower than 0.
        Element values are equal and is in the same index.
        Returns the same length data comparing to original data
        Returning list is same type as we want(np.ndarray)
        '''
        
        original = np.array(self.df["TR-UO"][1:])
        
        test = UO(self.low,self.close,self.high).trueRange()
                
        self.assertAlmostEqual(original[25],test[25])
        
        self.assertGreaterEqual(np.nanmin(test),0)  

        self.assertEqual(len(original),len(test)) 

        self.assertIsInstance(test,np.ndarray)

    

    def test_A7(self):
        '''
        In this module, testing the following things:
        7-Days Average can not be lower than 0.
        Element values are equal and is in the same index.
        Returns the same length data comparing to original data
        Returning list is same type as we want(np.ndarray)
        '''
        
        original = np.array(self.df["A7-UO"])
        
        test = UO(self.low,self.close,self.high).Average7()
                
        self.assertAlmostEqual(original[32],test[25])
        
        self.assertGreaterEqual(np.nanmin(test),0)  
        
        self.assertEqual(len(original[7:]),len(test)) 

        self.assertIsInstance(test,np.ndarray)

    

    def test_A14(self):
        '''
        In this module, testing the following things:
        14-Days Average can not be lower than 0.
        Element values are equal and is in the same index.
        Returns the same length data comparing to original data
        Returning list is same type as we want(np.ndarray)
        '''
        original = np.array(self.df["A14-UO"])
        
        test = UO(self.low,self.close,self.high).Average14()
                
        self.assertAlmostEqual(original[39],test[25])
        
        self.assertGreaterEqual(np.nanmin(test),0)  
        
        self.assertEqual(len(original[14:]),len(test)) 

        self.assertIsInstance(test,np.ndarray)

    
    def test_A28(self):
        '''
        In this module, testing the following things:
        28-Days Average can not be lower than 0.
        Element values are equal and is in the same index.
        Returns the same length data comparing to original data
        Returning list is same type as we want(np.ndarray)

        '''
        
        original = np.array(self.df["A28-UO"])
        
        test = UO(self.low,self.close,self.high).Average28()
                
        self.assertAlmostEqual(original[63],test[35])
        
        self.assertGreaterEqual(np.nanmin(test),0)  
        
        self.assertEqual(len(original[28:]),len(test)) 

        self.assertIsInstance(test,np.ndarray)
    
    

    def test_ultimateOscillator(self):
        '''
        In this module, testing the following things:
        Ultimate Average can not be lower than 0.
        Ultimate Average can not be greater than 100. 
        Element values are equal and is in the same index.
        Returns the same length data comparing to original data
        Returning list is same type as we want(np.ndarray)
        '''
        
        original = np.array(self.df["UO"])
        
        test = UO(self.low,self.close,self.high).uo()
                
        self.assertAlmostEqual(original[63],test[35])
        
        self.assertGreaterEqual(np.nanmin(test),0)

        self.assertLessEqual(np.nanmax(test),100)
        
        self.assertEqual(len(original[28:]),len(test)) 

        self.assertIsInstance(test,pd.Series)
    
if __name__ == "__main__":
    unittest.main()
