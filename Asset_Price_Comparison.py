# Compares the daily adjusted close price of two assets.
# Requires usage of YF_Pruner module to pull asset prices from Yahoo Finance!

import YF_Pruner as yfp
import datetime as dt
import matplotlib.pyplot as plt

def asset_comparison(ticker, startdate, enddate):
    """
    Returns the adjusted daily close prices of the assets using the YF_Pruner module.
    Missing price data is forward-filled.
    """
    data = yfp.get_daily_adj_close(ticker, startdate, enddate)
    data = data.ffill(axis=0)
    return data

def comparison_plot(data):
    """
    Plots the prices of the assets.
    """
    fig, ax = plt.subplots(figsize=(12,6))

    # Plots the price data from the first ticker
    ax.plot(data.index, data['Adj Close'].iloc[0:, 0], color='blue')
    ax.set_ylabel('Price ($)')
    ax.set_xlabel('Date')
    ax.legend([data['Adj Close'].columns[0]], loc='upper center')

    # Plots the price data from the second ticker
    ax2 = ax.twinx()
    ax2.set_ylabel('Price ($)')
    ax2.plot(data.index, data['Adj Close'].iloc[0:, 1], color='orange')
    ax2.legend([data['Adj Close'].columns[1]], loc='upper right')

    plt.show()