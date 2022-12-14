import pandas as pd
import unittest

from hyta.momentum import Momentum
class TestMomentum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data= pd.read_excel('files/momentum.xlsx')        
        cls.closes_list=  cls.data['cloeses_list'].to_list()        
        cls.result = cls.data['result'].to_list()
        cls.period = cls.data['period'].to_list()

    @classmethod
    def tearDownClass(cls):
        del cls.closes_list
        del cls.result
        del cls.period

    def test_momentum_input(self):
        # check input type
        self.assertIsNotNone(self.closes_list[47])
        self.assertIsInstance(self.closes_list[1],float)
        self.assertIsInstance(self.closes_list,list)

        # check  period
        self.assertIsInstance(self.period[1],int)
        self.assertGreater(self.period[4],0)

    def test_momentum_result(self):
        
        M = Momentum(self.closes_list,5)
        #check the value of result
        
        #if you find result right result, you must write period-1 for this test.It is not rural.
        #I set it. Becasue, period must not be 0 ,so 1st period's answer is at 0 index , 2st period's answer is at 1st index ....
        self.assertAlmostEqual(self.result[4],M.momentum(),2)
        self.assertNotAlmostEqual(self.result[5],M.momentum(),2)
        
        #check the type of result
        self.assertIsInstance(M.momentum(),float)

        #momentum never create None. check none result
        self.assertIsNotNone(M.momentum())
