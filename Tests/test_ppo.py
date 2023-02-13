import unittest
import pandas as pd 
from hyta.ppo import PPO

class TestPPO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.read_excel('Tests/files/PPO.xls')

    @classmethod
    def tearDownClass(cls):
        del cls.data
    
    def setUp(self) -> None:
        self.close = self.data["Close"]
        self.ppo_data = PPO(close=self.close)

    def test_ema12(self):
        self.result_ema12 = self.ppo_data.ema_12()
        self.assertAlmostEqual(self.result_ema12[1],self.ppo_data['EMA(12)'][1])
    
    def test_ema26(self):
        self.result_ema26 = self.ppo_data.ema_26()
        self.assertAlmostEqual(self.result_ema26[1],self.ppo_data['EMA( 26)'][1])
    
    def ppo(self):
        self.result_ppo = self.ppo_data.ppo()
        self.assertAlmostEqual(self.result_ppo[1],self.ppo_data['EMA( 26)'][1])
        

if __name__ == "__main__":
    unittest.main()
