import pandas as pd


class PPO:
    def __init__(self, close):
        self.close = close
        self.ppo_data = pd.DataFrame({"Close": self.close})

    def ema_12(self) -> pd.Series:
        weight_p_12 = round(2 / (12 + 1), ndigits=6)

        first = self.ppo_data["Close"][0]
        ema_12_ilk = (self.ppo_data["Close"][1] * weight_p_12) + (
            first * (1 - weight_p_12)
        )

        self.ppo_data["Ema_12"] = 0
        self.ppo_data.loc[:2, "Ema_12"] = pd.Series([first, ema_12_ilk])

        for i in range(1, len(self.ppo_data["Close"])):
            ema_12_ilk = (self.ppo_data["Close"][i] * weight_p_12) + (
                self.ppo_data["Ema_12"][i - 1] * (1 - weight_p_12)
            )
            self.ppo_data["Ema_12"][i:] = ema_12_ilk
        return pd.Series(self.ppo_data["Ema_12"])

    def ema_26(self) -> pd.Series:
        weight_p_26 = round(2 / (26 + 1), ndigits=6)

        first = self.ppo_data["Close"][0]
        ema_26_ilk = (self.ppo_data["Close"][1] * weight_p_26) + (
            first * (1 - weight_p_26)
        )

        self.ppo_data["Ema_26"] = 0
        self.ppo_data.loc[:2, "Ema_26"] = pd.Series([first, ema_26_ilk])

        for i in range(1, len(self.ppo_data["Close"])):
            ema_26_ilk = (self.ppo_data["Close"][i] * weight_p_26) + (
                self.ppo_data["Ema_26"][i - 1] * (1 - weight_p_26)
            )
            self.ppo_data["Ema_26"][i:] = ema_26_ilk
        return pd.Series(self.ppo_data["Ema_26"])

    def ppo(self) -> pd.Series:
        self.ema_12()
        self.ema_26()
        self.ppo_data["PPO"] = (
            (self.ppo_data["Ema_12"] - self.ppo_data["Ema_26"])
            / self.ppo_data["Ema_12"]
        ) * 100
        return pd.Series(self.ppo_data["PPO"])
