import talib as ta
import pandas as pd
import sklearn
def load_csv(input_file):
    return pd.read_csv(input_file)
MACD_FAST = 12
MACD_SLOW = 26

def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

if __name__ == '__main__':
    a = load_csv("data.csv")
    # print(a["Low"])
    high = a["High"].values
    low = a["Low"].values
    close = a["Close"].values
    open = a["Open"].values
    volumn = a["Volume"].apply(value_to_float).values
    # rsi
    rsi = ta.RSI(close)
    # macd
    macd, macd_signal_line, macd_hist = ta.MACD(close)
    ppo = ta.PPO(close)
    adx = ta.ADX(high, low, close)
    mom = ta.MOM(close)
    cci = ta.CCI(high,low,close)
    roc = ta.ROC(close)
    stok, stod = ta.STOCH(high, low, close)
    williamR = ta.WILLR(high, low, close)
    sma20 = ta.SMA(close, timeperiod=20)
    sma50 = ta.SMA(close, timeperiod=50)
    sma100 = ta.SMA(close, timeperiod=100)
    ema20 = ta.EMA(close, timeperiod=20)
    ema50 = ta.EMA(close, timeperiod=50)
    ema100 = ta.EMA(close, timeperiod=100)
    upper_band, middle_band, lower_band = ta.BBANDS(close)
    psar = ta.SAR(high,low)
    obv = ta.OBV(close, volumn)
    chaikin = ta.ADOSC(high,low, close, volumn)
    mfi = ta.MFI(high,low, close, volumn)
    atr = ta.ATR(high, low, close)

