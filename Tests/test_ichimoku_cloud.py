import unittest
import pandas as pd
from hyta.ichimoku_cloud import IchimokuCloud



class TestIchimokuCloud(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls) -> pd.Series:
        
        cls.data = pd.read_excel('Tests/data.xlsx')
        cls.close = cls.data['close'].to_list()
        cls.high = cls.data['high'].to_list()
        cls.low = cls.data['low'].to_list()
        cls.ts = cls.data['tenka_sen'].to_list()
        cls.ks = cls.data['kiju_sen'].to_list()
        cls.spa = cls.data['senkau span a'].to_list()
        cls.spb = cls.data['senkau span b'].to_list()
        cls.cs = cls.data['cikou span'].to_list()
        cls.all = [pd.Series([cls.ts[e],cls.ks[e],cls.spa[e],cls.spb[e],cls.cs[e]],["Tenkan Sen","Kijun Sen","Senkou Span A","Senkou Span B","Cikou Span"]) for e in range(len(cls.close))]

    @classmethod
    def tearDownClass(cls):
        del cls.data
        del cls.close
        del cls.high
        del cls.low
        del cls.ts
        del cls.ks
        del cls.spa
        del cls.spb
        del cls.cs
        del cls.all
        
    
    def test_ichimoku_cloud_result(self):
        

        ic = IchimokuCloud(self.close,self.low,self.high)

        #test_tenka_sen(self):        
        self.assertAlmostEqual(ic.ichimoku_cloud()[0],self.all[-1][0])
        self.assertIsInstance(ic.ichimoku_cloud()[0],float)
        self.assertGreater(ic.ichimoku_cloud()[0],0)
        #test_kijun_sen(self):        
        self.assertAlmostEqual(ic.ichimoku_cloud()[1],self.all[-1][1])
        self.assertIsInstance(ic.ichimoku_cloud()[1],float)
        self.assertGreater(ic.ichimoku_cloud()[1],0)
        #test_sekou_span_a        
        self.assertAlmostEqual(ic.ichimoku_cloud()[2],self.all[-1][2])
        self.assertIsInstance(ic.ichimoku_cloud()[2],float)
        self.assertGreater(ic.ichimoku_cloud()[2],0)
        #test_senkou_span_b        
        self.assertAlmostEqual(ic.ichimoku_cloud()[3],self.all[-1][3])
        self.assertIsInstance(ic.ichimoku_cloud()[3],float)
        self.assertGreater(ic.ichimoku_cloud()[3],0)
        #test_cikou_span_a        
        self.assertAlmostEqual(ic.ichimoku_cloud()[4],self.all[-1][4])
        self.assertIsInstance(ic.ichimoku_cloud()[4],float)
        self.assertGreater(ic.ichimoku_cloud()[4],0)

        #test ichimoku cloud
        self.assertIsInstance(ic.ichimoku_cloud(), pd.Series)
        self.assertEqual(len(ic.ichimoku_cloud()),len(self.all[-1]))
        
    def test_input_value(self):
        self.assertIsNotNone(self.close[100])
        self.assertIsNotNone(self.low[0])
        self.assertIsNotNone(self.high[1435])
        self.assertIsInstance(self.close, list)
        self.assertIsInstance(self.low, list)
        self.assertIsInstance(self.high, list)
        
        




if __name__ == '__main__':
    unittest.main()


