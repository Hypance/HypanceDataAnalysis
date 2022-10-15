import numpy as np
import pandas as pd

class CMO:
    '''
    This class calculate CMO for default 10-days period.

    It needs to get 'close' values and period(optional).
    
    '''
    def __init__(self,close:list,period:int=10) -> None:
        self.period = period
        self.close = close
    
    '''
    From period, returns a list
    by using cumulative function.
    Sum of the difference between the current close
    and previous close on up days for the specified period. 
    Up days are days when the current close is greater than the previous close.
    '''
    def cumulativeUp(self):
        up = [0]
        retUp = np.full(10,np.nan)
        for i in range(1,len(self.close)):
            if self.close[i]>self.close[i-1]:
                upT = self.close[i] - self.close[i-1]
                up.append(upT)
            else:
                up.append(0)

        cumulativeUp = np.cumsum(up)

        for i in range(0,len(cumulativeUp)-self.period):
            retUp = np.append(retUp,cumulativeUp[i+self.period]-cumulativeUp[i])

        return np.array(retUp)
    '''
    From period, returns a list
    by using cumulative function.
    Sum of the absolute value of the difference between the current close 
    and the previous close on down days for the specified period.
    Down days are days when the current close is less than the previous close.
    '''    
    
    def cumulativeDown(self):
        down = np.zeros(1)
        retDown = np.full(10,np.nan)
        for i in range(1,len(self.close)):
            if self.close[i]<self.close[i-1]:
                downT = abs(self.close[i]-self.close[i-1])
                down = np.append(down,downT)
            else:
                down = np.append(down,0)

        cumulativeDown = np.cumsum(down)

        for i in range(0,len(cumulativeDown)-self.period):
            retDown = np.append(retDown,cumulativeDown[i+self.period]-cumulativeDown[i])
        
        return retDown

    '''
    Running function for the class.
    '''
    def cmo(self) -> np.ndarray:
        
        retUp = self.cumulativeUp()
        retDown = self.cumulativeDown()
        cmo = ((retUp-retDown)/(retDown+retUp))*100
        return cmo