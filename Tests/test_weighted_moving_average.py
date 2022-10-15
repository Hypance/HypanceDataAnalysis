import unittest
from weighted_moving_average import WeightedMovingAverage


class TestWeightedMovingAverage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.close = [34.5, 34.5, 34.37, 34.56, 34.5, 34.37, 34.31, 34.31, 34.25, 34.37, 34.25, 34.12, 34.25, 34.19, 34.19, 33.94, 34.0, 33.75, 33.75, 34.25, 33.94, 34.25, 34.12, 34.5, 34.12, 34.0, 34.44, 34.25, 34.0, 34.31, 34.69, 34.81, 35.31, 35.19, 35.25, 36.0, 35.75, 35.75, 36.06, 36.5, 36.38, 36.62, 36.38, 36.5, 36.81, 37.0, 37.44, 37.5, 37.81, 37.63]
        cls.period= [2,3,4,5,6,7,8,9,10,11,12,40,32]
        cls.result = [37.69, 37.67, 37.64, 37.58, 37.52, 37.45, 37.38, 37.32, 37.26, 37.21, 37.16, 37.11, 37.06, 37.01, 36.96, 36.91, 36.86, 36.81, 36.76, 36.71, 36.65, 36.6, 36.54, 36.49, 36.44, 36.39, 36.34, 36.29, 36.25, 36.2, 36.16, 36.12, 36.07, 36.03, 35.99, 35.96, 35.92, 35.89, 35.85, 35.82, 35.79, 35.76, 35.73, 35.7, 35.68, 35.65, 35.63, 35.61]

    @classmethod
    def tearDownClass(cls):
        del cls.close
        del cls.period
        del cls.result

    def test_input_value(self):
        #period is always less than the lenght of close price list
        self.assertGreater(len(self.close),self.period[-2])
        self.assertLess(self.period[3],len(self.close))
        #close list type have to be list
        self.assertIsInstance(self.close, list)
        #period type have to be integer
        self.assertIsInstance(self.period[6], int)
        #period is never 0 and period and close's value is never None
        self.assertNotEqual(self.period[7],0)
        self.assertIsNotNone(self.period[0])
        self.assertIsNotNone(self.close[29])
        


    def test_wma(self):
        wma = WeightedMovingAverage(self.close,self.period[1])
        #check result value
        self.assertAlmostEqual(wma.weighted_moving_average(),self.result[1],2)
        self.assertNotAlmostEqual(wma.weighted_moving_average(), self.result[9])
        #check result type
        self.assertIsInstance(wma.weighted_moving_average(),float)
        self.assertNotIsInstance(wma.weighted_moving_average(), str)


        