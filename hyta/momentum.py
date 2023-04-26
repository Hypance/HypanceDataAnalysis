class Momentum:
    """
    Since the Momentum oscillator does not have an upper and lower boundary
    you must visually inspect the history of the momentum line and draw horizontal lines along its upper and lower boundaries.
    When the momentum line reaches these levels it may indicate that the stock may be overbought or oversold.
    The result is an indicator that oscillates around 100. Values less than 100 indicate negative momentum, or decreasing price, and vice versa.
    """

    def __init__(self, close_price_list, period: int):
        self.close_price_list = close_price_list
        self.period = period

    def momentum(self) -> float:
        # the formula of momentum
        return (self.close_price_list[-1] / self.close_price_list[-self.period]) * 100
