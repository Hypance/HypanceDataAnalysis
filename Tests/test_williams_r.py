import unittest
import pandas as pd

from hyta.williams_r import WilliamsR

class TestWiliiasR(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel('files/WilliamR.xlsx')
        cls.highs = cls.data['High'].to_list()
        cls.lowest = cls.data['Low'].to_list()
        cls.closes = cls.data['Current Close'].to_list()
        cls.result = cls.data['14R'].to_list()
                
    @classmethod
    def tearDownClass(cls):
        del cls.highs
        del cls.lowest
        del cls.closes
        del cls.result
    
    def test_input_value(self):
        self.assertIsInstance(self.highs,list)
        self.assertIsInstance(self.lowest,list)
        self.assertIsInstance(self.closes[6],float)
        self.assertIsInstance(self.result[-1],float)
        self.assertGreater(self.result[8],-100)
        self.assertLess(self.result[10],0)
    
    
    def test_result_williams_r(self):
        r = WilliamsR(self.closes[-1],self.lowest,self.highs)
        
        #check if result is None
        self.assertIsNotNone(r.WILLIAMS_R())
        

        #check if result is in limit.
        self.assertGreater(r.WILLIAMS_R(),-100)
        self.assertLess(r.WILLIAMS_R(),0)

        #check output type
        self.assertIsInstance(r.WILLIAMS_R(),float)

        #check result value
        self.assertAlmostEqual(self.result[-1], r.WILLIAMS_R(),2)        
        