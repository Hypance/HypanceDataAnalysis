class WilliamsR:
    """ "
    #Williams%R say overbought and oversold
    #Williams%R answer is between 0 to -100.
    #If anwer goes above -20, this is overbought. If it drops below -80, this is oversold
    #If answer is above -20 and moving below -20, It's a sign that the price might go down.
    #If answer is below -80 and rising above -80, It's a sign that the price might rise.
    #-10 and -90 reference values are more reliable than -20 and -80

    """

    def __init__(self, current_close: float, lowest_list: list, higest_list: list):
        self.current_close = current_close
        self.lowest_list = lowest_list
        self.higest_list = higest_list

    def __founder_higest_price(self):
        # This function find the higest price of the last 14 days
        return float(max(self.higest_list[-1:-15:-1]))

    def __founder_lowest_price(self):
        # This function find the lowest price of the last 14 days
        return float(min(self.lowest_list[-1:-15:-1]))

    def WILLIAMS_R(self):
        # The formula of Williams%R
        R = (
            (self.__founder_higest_price() - self.current_close)
            / (self.__founder_higest_price() - self.__founder_lowest_price())
            * -100
        )

        return R
