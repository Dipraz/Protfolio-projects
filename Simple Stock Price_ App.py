#!/usr/bin/env python
# coding: utf-8
#dip07.raz@gmail.com
# In[26]:


import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")


# In[27]:


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'


# In[28]:


#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)


# In[29]:


#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2023-12-31')


# In[30]:


# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)


# In[ ]:




