import unittest
import pandas as pd
from hyta.weighted_moving_average import WeightedMovingAverage


class TestWeightedMovingAverage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel('files/wma.xlsx')
        cls.close = cls.data['close'].to_list()
        cls.period= cls.data['period'].to_list()
        cls.result = cls.data['result'].to_list()
    @classmethod
    def tearDownClass(cls):
        del cls.data
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


        