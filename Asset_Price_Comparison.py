# Compares the daily adjusted close price of two assets.
# Requires usage of YF_Pruner module to pull asset prices from Yahoo Finance!

import YF_Pruner as yfp
import datetime as dt
import matplotlib.pyplot as plt

def asset_comparison(ticker, startdate, enddate):
      """
      Returns the adjusted daily close prices of the assets using the YF_Pruner module.
      Missing price data is forward-filled.

      Parameters
      ----------
      data :   'pd.DataFrame'
            The DataFrame containing prices for each series
      startdate :   'datetime'
            The start date for asset prices returned from Yahoo Finance!
      enddate :   'datetime'
            The end date for asset prices returned from Yahoo Finance!
      """
      data = yfp.get_daily_adj_close(ticker, startdate, enddate)
      data = data.ffill(axis=0)
      return data

def price_comparison_plot(data):
      """
      Plots the prices of the assets.

      Parameters
      ----------
      data :   'pd.DataFrame'
            The DataFrame containing prices for each series
      """
      fig, ax = plt.subplots(figsize=(12,6))

      # Plots the price data from the first ticker
      ax.plot(data.index, data.iloc[0:, 0], color='blue', label=data.columns[0])
      ax.set_ylabel(data.columns[0])
      ax.set_xlabel('Date')
      ax.legend([data.columns[0]], loc='upper left')

      # Plots the price data from the second ticker
      ax2 = ax.twinx()
      ax2.set_ylabel(data.columns[1])
      ax2.plot(data.index, data.iloc[0:, 1], color='orange', label=data.columns[1])
      ax2.legend([data.columns[1]], loc='lower left')

      plt.title('Price Movement of %s and %s' % (data.columns[0], data.columns[1]))
      plt.show()

def scatter_plot(data, y_ts, x_ts):
      """
      Plot a scatter plot of both time series for the provided DataFrames.

      Parameters
      ----------
      data  :   'pd.DataFrame'
            The DataFrame containing prices for each series
      ts1 :   'str'    
            The first time series column name -  tuple of multi-index column e.g. [('Adj Close', 'COLUMN_NAME')]
      ts2 :   'str'
            The second time series column name -  tuple of multi-index column e.g. [('Adj Close', 'COLUMN_NAME')]
      """
      plt.figure(figsize=(12,6))
      plt.xlabel('%s Price ($)' % data[x_ts].name)
      plt.ylabel('%s Price ($)' % data[y_ts].name)
      plt.title('%s and %s Price Scatterplot' % (data[y_ts].name, data[x_ts].name))
      plt.scatter(data[x_ts], data[y_ts])
      plt.show()

def pearson_corr(data):
      """
      Returns the Pearson correlation for two (stationary) time series data. 
      More appropriately used over asset price than returns.

      Parameters
      ----------
      data :   'pd.DataFrame'
            The DataFrame containing prices for each series
      
      Return
      ------
      Pearson correlation between the time series.
      """
      numer =  ((data.iloc[0:, 0] - data.iloc[0:, 0].mean()) * (data.iloc[0:, 1] - data.iloc[0:, 1].mean())).sum()
      denom = (((data.iloc[0:, 0] - data.iloc[0:, 0].mean())**2).sum() * ((data.iloc[0:, 1] -  data.iloc[0:, 1].mean())**2).sum())**0.5
      print('Pearson correlation of %s and %s: %s' % (data.columns[0], data.columns[1], round((numer/denom), 5)))

def qd_corr(data):
      """
      Returns the QuantDare correlation for two (stationary) time series data.
      Difference with the Pearson correlation is the mean of the series 
      is removed from the calculation.
      More appropriately used over asset returns than price.

      Parameters
      ----------
      data :   'pd.DataFrame'
            The DataFrame containing prices for each series
      
      Return
      ------
      QuantDare correlation between the time series.
      """
      numer = (data.iloc[0:, 0]*data.iloc[0:, 1]).sum()
      denom = (((data.iloc[0:, 0])**2).sum() * ((data.iloc[0:, 1])**2).sum())**0.5
      print('QuantDare correlation of %s and %s: %s' % (data.columns[0], data.columns[1], round((numer/denom), 5)))