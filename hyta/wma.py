class WeightedMovingAverage:
    """
    A Weighted Moving Average puts more weight on recent data and less on past data.
    This is done by multiplying each bar’s price by a weighting factor.
    """

    def __init__(self, close_list: list, period: int):
        self.close_list = close_list
        self.period = period

    def weighted_moving_average(self) -> float:
        # the formula of wma
        # P1 = current close price, Pn = n days ago close price
        # wma = P1*n + P2*(n-1) + ..... + Pn*1 / n + (n-1) + ..... +1
        top_wma = 0
        bottom_wma = 0
        for i in range(1, self.period + 1):
            top_wma += self.close_list[-i] * (self.period + 1 - i)
            bottom_wma += i

        return top_wma / bottom_wma
