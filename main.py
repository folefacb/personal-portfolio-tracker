import numpy as np 
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st


st.title("Investment Portfolio Dashboard")

assets = st.text_input("Provide your assets (comma-seperated)", "AAPL, MSFT, GOOGL")

start = st.date_input("Pick a starting date for your analysis", 
                      value = pd.to_datetime('2022-06-01'))

data = yf.download(assets, start=start)['Adj Close']

ret_df = data.pct_change()

cumul_ret = (ret_df + 1).cumprod() - 1
pf_cumul_ret = cumul_ret.mean(axis=1)

benchmark = yf.download('^GSPC',start=start)['Adj Close']
bench_ret = benchmark.pct_change()
bench_dev = (bench_ret + 1).cumprod() - 1

W= (np.ones(len(ret_df.cov()))/len(ret_df.cov()))

pf_std = (W.dot(ret_df.cov()).dot(W)) ** (1/2)

st.subheader("Porfolio vs. Index Development")

tog = pd.concat([bench_dev, pf_cumul_ret],axis=1)

tog.columns = ['S&P500 Peformance', 'Portfolio Peformance']

st.subheader("Porfolio risk")
pf_std

st.subheader("Benchmark RIsk:")
bench_risk = bench_ret.std()

st.subheader("Porfolio Composition:")

fig, ax = plt.subplots(facecolor = '#121212')
ax.pie(W, labels=data.columns, autopct = '%1.1f%%', textprops={'color': 'white'})

st.pyplot(fig)
