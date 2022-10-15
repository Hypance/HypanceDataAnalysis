import unittest


from hyta.williams_r import WilliamsR

class TestWiliiasR(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        
        cls.highs = [127.009,127.6159,126.5911,127.3472,128.173,128.4317,127.3671,126.422,126.8995,126.8498,125.646,125.7156,127.1582,127.7154,127.6855,128.2228,128.2725,128.0934,128.2725,127.7353,128.77,129.2873,130.0633,129.1182,129.2873,128.4715,128.0934,128.6506,129.1381,128.6406]
        cls.lowest = [125.3574,126.1633,124.9296,126.0937,126.8199,126.4817,126.034,124.8301,126.3921,125.7156,124.5615,124.5715,125.0689,126.8597,126.6309,126.8001,126.7105,126.8001,126.1335,125.9245,126.9891,127.8148,128.4715,128.0641,127.6059,127.596,126.999,126.8995,127.4865,127.397]
        cls.closes = [127.2876,127.1781,128.0138,127.1085,127.7253,127.0587,127.3273,128.7103,127.8745,128.5809,128.6008,127.9342,128.1133,127.596,127.596,128.6904,128.2725]
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
        self.assertTrue(type(r.WILLIAMS_R()) == float)

        #check result value
        self.assertAlmostEqual(self.result[-1], round(r.WILLIAMS_R(),2))        
        



if __name__ == '__main__':
    unittest.main()