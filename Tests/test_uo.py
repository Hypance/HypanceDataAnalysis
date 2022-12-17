import pandas as pd 
import numpy as np 
import unittest 
from hyta.uo import UO

class TestUltimateOscillator(unittest.TestCase):
    """
    In all tests;
    Element values are to be equal and is in the same index,
    The same length data is returned compared to original data
    Correct dtype is returned (np.ndarray)
    MA is not to be lower than 0
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.read_excel("Tests/files/UO-datas.xlsx")
        cls.close = np.array(cls.df["close"])
        cls.high = np.array(cls.df["high"])
        cls.low = np.array(cls.df["low"])

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.df

    # Buying Pressure can not be negative number.
    def test_buyingPressure(self):
        original = np.array(self.df["BP-UO"][1:])
        test = UO(self.low,self.close,self.high).buyingPressure()
        self.assertAlmostEqual(original[-1],test[-1]) 
        self.assertGreaterEqual(np.nanmin(test),0)   
        self.assertEqual(len(original),len(test)) 
        self.assertIsInstance(test,np.ndarray)

    # True Range can not be lower than 0.
    def test_trueRange(self):
        original = np.array(self.df["TR-UO"][1:])
        test = UO(self.low,self.close,self.high).trueRange()
        self.assertAlmostEqual(original[-1],test[-1]) 
        self.assertGreaterEqual(np.nanmin(test),0)  
        self.assertEqual(len(original),len(test)) 
        self.assertIsInstance(test,np.ndarray)

    # 7-Days Average can not be lower than 0.
    def test_A7(self):
        original = np.array(self.df["A7-UO"])
        test = UO(self.low,self.close,self.high).Average7()
        self.assertAlmostEqual(original[-1],test[-1]) 
        self.assertGreaterEqual(np.nanmin(test),0)  
        self.assertEqual(len(original[7:]),len(test)) 
        self.assertIsInstance(test,np.ndarray)

    # 14-Days Average can not be lower than 0.
    def test_A14(self):
        original = np.array(self.df["A14-UO"])
        test = UO(self.low,self.close,self.high).Average14()
        self.assertAlmostEqual(original[-1],test[-1]) 
        self.assertGreaterEqual(np.nanmin(test),0)  
        self.assertEqual(len(original[14:]),len(test)) 
        self.assertIsInstance(test,np.ndarray)
    
    # 28-Days Average can not be lower than 0.
    def test_A28(self):
        original = np.array(self.df["A28-UO"])
        test = UO(self.low,self.close,self.high).Average28()
        self.assertAlmostEqual(original[-1],test[-1]) 
        self.assertGreaterEqual(np.nanmin(test),0)  
        self.assertEqual(len(original[28:]),len(test)) 
        self.assertIsInstance(test,np.ndarray)    

    def test_ultimateOscillator(self):
        '''
        Ultimate Average can not be lower than 0.
        Ultimate Average can not be greater than 100. 
        '''
        original = np.array(self.df["UO"])
        test = UO(self.low,self.close,self.high).uo()
        self.assertAlmostEqual(original[-1],test.iloc[-1]) 
        self.assertGreaterEqual(np.nanmin(test),0)
        self.assertLessEqual(np.nanmax(test),100)
        self.assertEqual(len(original[28:]),len(test)) 
        self.assertIsInstance(test,pd.Series)
    
if __name__ == "__main__":
    unittest.main()
