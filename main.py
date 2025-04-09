import numpy as np 
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st


st.title("Investment Portfolio Dashboard")

assets = st.text_input("Provide your assets (comma-seperated)", "AAPL, MSFT, GOOGL")

start = st.date_input("Pick a starting date for your analysis", value = pd.to_datetime('2022-06-01'))

data = yf.download(assets, start=start)['Adj Close']

print(data)
