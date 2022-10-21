import unittest
import pandas as pd
from hyta.stochasticoscillator import StochasticOscillator

class TestStochasticOscillator(unittest.TestCase):

  PATH="files/StochasticOscillator.xlsx"

  @classmethod
  def setUpClass(cls):
    cls.data=pd.read_excel(cls.path) 

  @classmethod
  def tearDownClass(cls):
    del cls.data
    del cls.close
    del cls.low
    del cls.high

  def setUp(self)->None:
    self.close=self.data["Close"]
    self.low=self.data["Low"]
    self.high=self.data["High"]
    self.fast_stochastic=self.data["fast_stochastic"]
    self.slow_stochastic=self.data["slow_stochastic"]

  def test_fast_stochastic(self):
    self.assertAlmostEqual(self.fast_stochastic[1],self.data["fast_stochastic"][1])
    self.assertGreater=self.data["fast_stochastic",-1]
    self.assertLess=self.data["fast_stochastic",1]
    
  def slow_stochastic(self):
    self.assertAlmostEqual(self.slow_stochastic[1],self.data["slow_stochastic"][1])
    self.assertGreater=self.data["slow_stochastic",-1]
    self.assertLess=self.data["slow_stochastic",1]
    

if__name__ =='__main__':
    unittest.main()
