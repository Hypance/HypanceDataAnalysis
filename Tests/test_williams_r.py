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
        cls.result = [-29.56,-32.39,-10.80,-34.19,-18.25,-35.48,-25.47,-1.42,-29.90,-26.94,-26.58,-38.77,-39.04,-59.61,-59.61,-33.17,-43.27]
                
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
        



if __name__ == '__main__':
    unittest.main()