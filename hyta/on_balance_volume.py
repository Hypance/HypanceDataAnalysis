class OnBalanceVolume:
    """On Balance Volume is calculated by adding the day's volume to a cumulative total when the security's price
    closes up, and subtracting the day's volume when the security's price closes down.

    If today's close is greater than yesterday's close then:
    OBV = Yesterday’s OBV + Today’s Volume

    If today’s close is less than yesterday’s close then:
    OBV = Yesterday’s OBV - Today’s Volume

    If today’s close is equal to yesterday’s close then:
    OBV = Yesterday’s OBV
    """

    def __init__(self, close_list, volume_list, period):
        self.close_list = close_list
        self.volume_list = volume_list
        self.period = period

    def on_balance_volume(self):
        main_obv = self.volume_list[-self.period]
        # first day OBV is first day value
        for main_period in range(self.period - 1, 0, -1):
            if self.close_list[-main_period] > self.close_list[-main_period - 1]:
                main_obv += self.volume_list[-main_period]

            elif self.close_list[-main_period] < self.close_list[-main_period - 1]:
                main_obv -= self.volume_list[-main_period]

            elif self.close_list[-main_period] == self.close_list[-main_period - 1]:
                main_obv += 0

        return main_obv
