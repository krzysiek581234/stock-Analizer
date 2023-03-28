import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as pyo
from datetime import datetime

def MACD (EMA12 , EMA26):
    MACDR = np.zeros_like(EMA12)
    for i in range(len(EMA12)):
        MACDR[i] = EMA12[i] - EMA26[i]
    return MACDR

def EMA(arr, n):
    k = 2 / (n + 1)
    ema = np.zeros_like(arr)
    #ADD  FIRST ELEMENT TO EMA
    for i in range(0 ,n):
        ema[i] = arr[i]
    for value in range(n ,len(arr)):
        licznik = arr[value]
        denominator = 1
        for i in range(1, n):
            denominator += (1 - k)**i # mianownik
            if value - i >= 0:
                licznik += arr[value - i] * (1 - k)**i # licznik
        ema[value] = licznik/denominator
    return ema

def print_plot(df, EMA12, EMA26, EMA100):
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Close'], label='normal')
    plt.xticks(df['Date'][::500])
    ax.plot(EMA12, label='EMA12')
    ax.plot(EMA26, label='EMA26')
    ax.plot(EMA100, label='EMA100')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.legend(loc='upper left')
    ax.set_title('AMD close Prices')
    plt.show()

import plotly.graph_objects as go

def print_plotflex(df, EMA12, EMA26, EMA100):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='normal'))
    fig.add_trace(go.Scatter(x=df['Date'], y=EMA12, name='EMA12'))
    fig.add_trace(go.Scatter(x=df['Date'], y=EMA26, name='EMA26'))
    fig.add_trace(go.Scatter(x=df['Date'], y=EMA100, name='EMA100'))
    fig.update_layout(title='AMD close Prices', xaxis_title='Date', yaxis_title='Price')
    fig.show()


def print_MACD(MACD):
    SIGNAL = EMA(MACD, 9)
    plt.plot(SIGNAL)
    plt.plot(MACD)
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pd.read_csv('AMD.csv')

    orginaldata = df["Close"].tolist()
    EMA12 = EMA(orginaldata, 12)
    EMA26 = EMA(orginaldata, 26)
    EMA100 = EMA(orginaldata, 100)
    MACD = MACD(EMA12, EMA26)
    print_MACD(MACD)
    print_plot(df, EMA12, EMA26, EMA100)
    print_plotflex(df, EMA12, EMA26, EMA100)


