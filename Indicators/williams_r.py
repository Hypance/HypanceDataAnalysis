class WilliamsR:

    def __init__(self, current_close:float=1, lowest_list:float=14, higest_list:float=14):
        self.current_close = current_close
        self.lowest_list = lowest_list
        self.higest_list = higest_list

    def __founder_higest_price(self):
        #This function find the higest price of the last 14 days
        self.higest_price = float(max(self.higest_list[-1:-15:-1]))

    def __founder_lowest_price(self):
        #This function find the lowest price of the last 14 days
        self.lowest_price = float(min(self.lowest_list[-1:-15:-1]))

    def WILLIAMS_R(self):
        #Williams%R say overbought and oversold
        #Williams%R answer is between 0 to -100. 
        #If anwer goes above -20, this is overbought. If it drops below -80, this is oversold
        #If answer is above -20 and moving below -20, It's a sign that the price might go down.
        #If answer is below -80 and rising above -80, It's a sign that the price might rise.
        #-10 and -90 reference values ​​are more reliable than -20 and -80

        # The formula of Williams%R
        R = (self.higest_price - self.current_close) / (self.higest_price - self.lowest_price) *-100
        
        return R
