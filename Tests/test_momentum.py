import string
from sys import float_repr_style
import unittest

from hyta.momentum import Momentum

class TestMomentum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):        
        cls.cloeses_list= [182.14, 144.48, 248.09, 217.85, 137.89, 267.24, 270.85, 254.74, 293.56, 176.19, 194.56, 146.28, 126.25, 193.21, 284.42, 126.93, 212.05, 150.97, 122.66, 103.76, 121.92, 135.94, 177.59, 253.27, 291.93, 190.6, 239.34, 128.3, 166.86, 197.6, 136.32, 218.97, 179.21, 217.63, 124.73, 156.6, 189.09, 298.05, 196.19, 189.87, 119.28, 212.93, 299.53, 276.85, 223.56, 282.96, 161.53, 189.29, 196.42, 258.66, 294.2, 100.75, 271.11, 257.04, 261.53, 242.59, 284.89, 169.57, 120.8, 176.3, 293.04, 151.62, 275.89, 183.91, 280.71, 151.48, 195.45, 144.59, 159.23, 277.57, 228.56, 108.35]              
        cls.result = [100.0, 47.41, 39.04, 68.05, 74.94, 55.44, 71.53, 38.6, 58.91, 39.27, 71.46, 36.97, 61.46, 89.69, 63.9, 38.03, 44.66, 41.43, 42.15, 39.97, 107.54, 36.83, 41.89, 55.16, 57.24, 67.08, 38.29, 48.47, 39.14, 36.17, 50.89, 90.84, 57.07, 55.23, 36.35, 57.3, 69.19, 86.87, 49.79, 60.46, 49.48, 79.48, 54.83, 64.93, 84.45, 45.27, 56.85, 37.12, 42.78, 61.01, 79.7, 88.87, 104.42, 88.33, 71.77, 51.1, 85.36, 38.1, 56.08, 85.82, 74.07, 55.69, 61.5, 36.91, 42.53, 40.0, 40.54, 78.58, 49.74, 43.67, 74.99]
        cls.period = [1,2,3,4,5,6,7,8,9,10,11,12]
    @classmethod
    def tearDownClass(cls):
        del cls.cloeses_list
        del cls.result
        del cls.period

    def test_momentum_input(self):
        # check input type
        self.assertIsNotNone(self.cloeses_list[47])
        self.assertIsInstance(self.cloeses_list[1],float)
        self.assertIsInstance(self.cloeses_list,list)

        # check  period
        self.assertIsInstance(self.period[1],int)
        self.assertGreater(self.period[4],0)

    def test_momentum_result(self):
        
        M = Momentum(self.cloeses_list,5)
        #check the value of result
        
        #if you find result right result, you must write period-1 for this test.It is not rural.
        #I set it. Becasue, period must not be 0 ,so 1st period's answer is at 0 index , 2st period's answer is at 1st index ....
        self.assertAlmostEqual(self.result[4],M.momentum(),2)
        self.assertNotAlmostEqual(self.result[5],M.momentum(),2)
        
        #check the type of result
        self.assertIsInstance(M.momentum(),float)

        #momentum never create None. check none result
        self.assertIsNotNone(M.momentum())

    

if __name__ == "__main__":
    unittest.main()