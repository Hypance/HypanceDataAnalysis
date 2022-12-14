import unittest
import pandas as pd
from hyta.Stochastic_Oscillator import StochasticOscillator

class TestStochasticOscillator(unittest.TestCase):

  PATH="files/StochasticOscillator.xlsx"

  @classmethod
  def setUpClass(cls):
    cls.data=pd.read_excel(cls.path)

  @classmethod
  def tearDownClass(cls):
    del cls.data
    

  def setUp(self)->None:
    so=StochasticOscillator(data["high"],data["low"],data["close"],periods=5)
    
  def tearDown(self):
    del so

  def test_fast_stochastic(self):
    self.assertAlmostEqual(so.fast_stochastic()[1],self.data["fast_stochastic"][1])
    self.assertGreater(so.fast_stochastic()[1],-1)
    self.assertLess(so.fast_stochastic()[4],1)
    
  def test_slow_stochastic(self):
    self.assertAlmostEqual(so.slow_stochastic()[1],self.data["slow_stochastic"][1])
    self.assertGreater(so.slow_stochastic()[1],-1)
    self.assertLess(so.slow_stochastic()[4],1)
    

if__name__ =='__main__':
    unittest.main()
