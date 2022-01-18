import numpy as np
import pandas as pd


# self = []

# if i do a class for imports.
# def __init__(self):
#    pass
prices = [0.019191, 0.018948, 0.019505, 0.020388, 0.019766, 0.019533, 0.019069, 0.019135,
          0.019827, 0.02049, 0.020074, 0.02069, 0.020919, 0.021062, 0.020547, 0.020795, 0.020836, 0.020774]
candles = [[1609322400, 0.01959, 0.019962, 0.019522, 0.019928, 62868647.6], [1609326000, 0.019863, 0.020218, 0.019404, 0.019461, 46113859.8], [1609329600, 0.019422, 0.019674, 0.019291, 0.019492, 58692350.6], [1609333200, 0.019484, 0.019725, 0.019355, 0.019355, 68193034.2], [1609336800, 0.019378, 0.019909, 0.0193, 0.019749, 31780333.4], [1609340400, 0.019749, 0.019829, 0.01947, 0.019717, 23396321.2], [1609344000, 0.019747, 0.019966, 0.019377, 0.019733, 30008367.5], [1609347600, 0.019717, 0.019891, 0.019625, 0.019851, 39410745.0], [1609351200, 0.019828, 0.019844, 0.019552, 0.019636, 48463521.9], [
    1609354800, 0.019612, 0.019933, 0.019549, 0.019845, 38420423.8], [1609358400, 0.019862, 0.019908, 0.019644, 0.019877, 49421175.6], [1609362000, 0.019947, 0.020007, 0.019573, 0.019732, 53716758.0], [1609365600, 0.019732, 0.019937, 0.019616, 0.019842, 51987557.7], [1609369200, 0.019827, 0.020298, 0.019762, 0.020238, 36866302.8], [1609372800, 0.020238, 0.020284, 0.019728, 0.019822, 36001887.0], [1609376400, 0.019867, 0.019907, 0.019238, 0.019454, 43506425.8], [1609380000, 0.019455, 0.019529, 0.019138, 0.019162, 46924659.4], [1609383600, 0.01917, 0.019176, 0.018712, 0.019095, 22064129.3]]


class test():
    def __init__(self):
        pass

    prices = [0.019191, 0.018948, 0.019505, 0.020388, 0.019766, 0.019533, 0.019069, 0.019135,
              0.019827, 0.02049, 0.020074, 0.02069, 0.020919, 0.021062, 0.020547, 0.020795, 0.020836, 0.020774]

    def RSI(self, prices, period=14):
        deltas = np.diff(prices)
        seed = deltas[:period+1]
        up = seed[seed >= 0].sum()/period
        down = -seed[seed < 0].sum()/period
        rs = up/down
        rsi = np.zeros_like(prices)
        rsi[:period] = 100. - 100./(1. + rs)

        for i in range(period, len(prices)):
            delta = deltas[i - 1]  # cause the diff is 1 shorter
            if delta > 0:
                upval = delta
                downval = 0.
            else:
                upval = 0.
                downval = -delta

            up = (up*(period - 1) + upval)/period
            down = (down*(period - 1) + downval)/period
            rs = up/down
            rsi[i] = 100. - 100./(1. + rs)
            if len(prices) > period:
                print("rsi2", rsi[i])
                print("rsi", rsi[-i])
                return rsi[i]

            else:
                return 50

    def ema(self, prices, period, key=False):
        if len(prices) <= period:
            period = len(prices)

        weights = np.exp(np.linspace(-1., 0., period))
        weights /= weights.sum()
        if key:
            pricePoints = np.asarray([c[key] for c in prices])
        else:
            pricePoints = np.asarray(prices)
        avg = np.convolve(pricePoints, weights, mode='full')[:len(pricePoints)]
        print("ema", avg[-1])
        return avg[-1]
    #
    #
    #
    #
    #   new stuff

    candles = [[1609322400, 0.01959, 0.019962, 0.019522, 0.019928, 62868647.6], [1609326000, 0.019863, 0.020218, 0.019404, 0.019461, 46113859.8], [1609329600, 0.019422, 0.019674, 0.019291, 0.019492, 58692350.6], [1609333200, 0.019484, 0.019725, 0.019355, 0.019355, 68193034.2], [1609336800, 0.019378, 0.019909, 0.0193, 0.019749, 31780333.4], [1609340400, 0.019749, 0.019829, 0.01947, 0.019717, 23396321.2], [1609344000, 0.019747, 0.019966, 0.019377, 0.019733, 30008367.5], [1609347600, 0.019717, 0.019891, 0.019625, 0.019851, 39410745.0], [1609351200, 0.019828, 0.019844, 0.019552, 0.019636, 48463521.9], [
        1609354800, 0.019612, 0.019933, 0.019549, 0.019845, 38420423.8], [1609358400, 0.019862, 0.019908, 0.019644, 0.019877, 49421175.6], [1609362000, 0.019947, 0.020007, 0.019573, 0.019732, 53716758.0], [1609365600, 0.019732, 0.019937, 0.019616, 0.019842, 51987557.7], [1609369200, 0.019827, 0.020298, 0.019762, 0.020238, 36866302.8], [1609372800, 0.020238, 0.020284, 0.019728, 0.019822, 36001887.0], [1609376400, 0.019867, 0.019907, 0.019238, 0.019454, 43506425.8], [1609380000, 0.019455, 0.019529, 0.019138, 0.019162, 46924659.4], [1609383600, 0.01917, 0.019176, 0.018712, 0.019095, 22064129.3]]
    for i in range(0, len(candles)-2):
        candles[i].pop(0)
        candles[i].pop(-1)

    def trueRange(self, candles):
        atr1 = atr2 = atr3 = 0
        candles = candles[-2:]
        atr1 = abs(candles[-1][2] - candles[-1][3])
        if len(candles) > 1:
            atr2 = abs(candles[-1][2] - candles[-2][4])
            atr3 = abs(candles[-1][3] - candles[-2][4])
            print('trueRange-', atr1, atr2, atr3)
        return max([atr1, atr2, atr3])

    def averageTrueRange(self, candles, window=14):
        # print(len(candles))
        if len(candles) < window:
            window = len(candles)

        trueRanges = []
        for i in range(0, window):
            if i > 0:
                trueRanges.append(self.trueRange(candles[-i-1:-i]))
            else:
                trueRanges.append(self.trueRange(candles[-1:]))
        atr = self.sma(trueRanges, window, False)
        print('averageTrueRange', atr)
        return atr

    def directionalMovement(self, candles, window=14):
        if len(candles) < window+2:
            window = len(candles)
        candles = candles[-(window+2):]
        highs = []
        lows = []
        closes = []
        pDMs = []
        nDMs = []
        for i in range(0, len(candles)):
            highs.append(candles[i][2])
            lows.append(candles[i][3])
            closes.append(candles[i][4])
            pDM = 0.0
            nDM = 0.0
            if i > 1:
                upMove = highs[i]-highs[i-1]
                dnMove = lows[i-1] - lows[i]
                if (upMove > dnMove) & (upMove > 0):
                    pDM = upMove
                if (dnMove > upMove) & (dnMove > 0):
                    nDM = dnMove
            pDMs.append(pDM)
            nDMs.append(nDM)
        ATR = self.averageTrueRange(candles, window)
        pDI = self.sma(pDMs, window)/ATR*100
        nDI = self.sma(nDMs, window)/ATR*100
        sum = pDI+nDI
        sum = 1 if sum == 0 else sum
        DX = abs(pDI-nDI)/sum*100
        return {'pDI': pDI, 'nDI': nDI, 'DX': DX}, highs, lows, closes

    def DMI(self, window=14, adxwindow=14, fillna=False):
        DMI = pd.DataFrame(columns=['pDI', 'nDI', 'DX', 'ADX'])
        upMove = self.directionalMovement(highs) - highs.shift()
        dnMove = lows.shift() - lows
        pDM = closes*0
        nDM = closes*0
        pDM[(upMove > dnMove) & (upMove > 0)] = upMove
        nDM[(dnMove > upMove) & (dnMove > 0)] = dnMove
        TR = self.trueRange(highs, lows, closes)
        ATR = self.sma(TR, window, fillna)
        pDI = self.sma(pDM)/ATR*100
        nDI = self.sma(nDM)/ATR*100
        sum = pDI+nDI
        sum[pDI+nDI == 0] = 1
        DX = abs(pDI-nDI)/sum*100
        ADX = self.sma(DX, adxWindow-1, fillna)
        DMI['pDI'] = pDI
        DMI['nDI'] = nDI
        DMI['DX'] = DX
        DMI['ADX'] = ADX
        print(DMI)
        print("hello")
        return DMI

    # smoothed Moving Average

    def sma(self, prices, window=14, key=False):
        if len(prices) < window:
            window = len(prices)
        if key:
            dataPoints = [c[key] for c in data[-window:]]
        else:
            dataPoints = prices[-window:]
        weights = np.repeat(1.0, window) / window
        print("sma")
        return np.convolve(dataPoints, weights, 'valid')[0]

    def DMI(self, highs, lows, closes, window=14, adxWindow=14, fillna=False):
        return
        # return self.DMI(highs, lows, closes, window, adxWindow, fillna)

    def MACD(self, prices, nslow=26, nfast=12):
        emaslow = self.ema(prices, nslow)
        emafast = self.ema(prices, nfast)
        return {
            'ema_slow': emaslow,
            'ema_fast': emafast,
            'macd': emafast - emaslow
        }


rsi1 = test()
rsi1.RSI(prices, period=14)
ema1 = test()
ema1.ema(prices, period=20, key=False)
ema1 = test()
ema1.ema(prices, period=55, key=False)
ema1 = test()
ema1.ema(prices, period=100, key=False)
tR1 = test()
tR1.trueRange(candles)
atr1 = test()
atr1.averageTrueRange(candles, window=14)
dm1 = test()
dm1.directionalMovement(candles, window=14)
dMI = test()
dMI.DMI(highs, lows, closes, window=14, adxWindow=14, fillna=False)
