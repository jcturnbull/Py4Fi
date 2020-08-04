#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:39:52 2020

@author: jacksonturnbull
"""

#page19, data pull invalid at of 6/2018
"""
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web

goog = web.DataReader('GOOG', data_source='google', start='3/14/2009', end='4/14/2014')
goog.tail()

goog['Log_ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = pd.rolling_std(goog['Log_ret'], window=252*np.sqrt(252))
%matplotlib inline
goog[['Close', 'Volatility']].plot(subplots=True, color='blue', figzie=(8,6))


"""

#from https://towardsdatascience.com/a-comprehensive-guide-to-downloading-stock-prices-in-python-2cd93ff821d4

import pandas as pd
import numpy as np
import yfinance as yf
#from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt

goog = yf.download('GOOG', start='2009-03-14', end='2014-04-15')
goog.tail()
goog['Log_ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = (goog['Log_ret']).rolling(window=252).std()*np.sqrt(252)
#goog[['Close', 'Volatility']].plot(subplots=True, color='blue')
#goog[['Close', 'Volatility']].loc['2010-03-16':'2014-04-15'].plot(subplots=True, color='blue')
goog.loc['2010-03-16':'2014-04-15',['Close', 'Volatility']].plot(subplots=True, color=('blue','green'))
#plt.subplot(211)
#plt.plot(goog['Close'])
#plt.subplot(212)
#plt.plot(goog['Volatility'])
plt.show()
#%matplotlib inline
#goog[['Close', 'Volatility']].plot(subplots=True, color='blue')

