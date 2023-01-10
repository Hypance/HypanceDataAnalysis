import unittest
import pandas as pd
from hyta.Stochastic_Oscillator import StochasticOscillator

class TestStochasticOscillator(unittest.TestCase):


  @classmethod
  def setUpClass(cls):
    cls.path="Tests/files/StochasticOscillator.xlsx"
    cls.data=pd.read_excel(cls.path)

  @classmethod
  def tearDownClass(cls):
    del cls.data
    

  def setUp(self)->None:
    self.high=self.data["high"]
    self.low=self.data["low"]
    self.close=self.data["close"]
    self.StochasticOscillator_data=StochasticOscillator(self.high,self.low,self.close)
    so=StochasticOscillator(data["high"],data["low"],data["close"],periods=5)
    
  def tearDown(self):
    del so

  def test_fast_stochastic(self):
    self.assertAlmostEqual(so.fast_stochastic()[10],self.data["fast_stochastic"][10])
    self.assertGreater(so.fast_stochastic()[15],-1)
    self.assertLess(so.fast_stochastic()[35],99)
    
  def test_slow_stochastic(self):
    self.assertAlmostEqual(so.slow_stochastic()[10],self.data["slow_stochastic"][10])
    self.assertGreater(so.slow_stochastic()[15],-1)
    self.assertLess(so.slow_stochastic()[37],99)
    

if __name__ =='__main__':
    unittest.main()
