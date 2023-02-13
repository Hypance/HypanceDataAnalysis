import numpy as np
from hyta.dx import DX

class ADX:
    def __init__(self,high,low,close):
        self.high = high
        self.low = low
        self.close = close

    def adx(self):
        dx_data1 = DX(high=self.high,low=self.low,close=self.close)
        dx_data = dx_data1.dx()
        dx_mean = dx_data[14:27].mean()
        
        adx_data = [np.nan,dx_mean]
        for i in range(27,len(dx_data)):
            adx_result = ((adx_data[-1] * 13)+ dx_data[i])/14
            adx_data.append(adx_result)
    
        return adx_data