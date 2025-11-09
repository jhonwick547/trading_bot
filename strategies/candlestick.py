# strategies/candlestick.py
def get_candle_signal(klines):
    if len(klines) < 2:
        return 0
    o1, c1 = float(klines[-2][1]), float(klines[-2][4])
    o2, c2 = float(klines[-1][1]), float(klines[-1][4])
    if c1 < o1 and c2 > o2 and c2 > c1 and o2 < o1:
        return 1
    if c1 > o1 and c2 < o2 and c2 < c1 and o2 > o1:
        return -1
    return 0
