import numpy as np 
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Investment Dashboard", layout="wide")

st.title("📈 Investment Portfolio Dashboard")

# --- User Input ---
assets_input = st.text_input("Provide your assets (comma-separated)", "AAPL, MSFT, GOOGL")
assets = [ticker.strip().upper() for ticker in assets_input.split(',') if ticker.strip()]
st.write("✅ Parsed Tickers:", assets)

start = st.date_input("Pick a starting date for your analysis", 
                      value=pd.to_datetime('2022-06-01'))

# --- Data Download ---
raw_data = yf.download(assets, start=start)

# Handle different formats of Adj Close
if 'Adj Close' in raw_data.columns:
    data = raw_data['Adj Close']
elif isinstance(raw_data.columns, pd.MultiIndex) and 'Adj Close' in raw_data.columns.levels[0]:
    data = raw_data['Adj Close']
else:
    st.error("❌ No 'Adj Close' column found in downloaded data. Check ticker symbols.")
    st.stop()

# Check if data is valid
if data is None or data.empty:
    st.error("❌ Failed to retrieve data. Please check your ticker symbols.")
    st.stop()

# --- Portfolio Returns ---
ret_df = data.pct_change()
cumul_ret = (ret_df + 1).cumprod() - 1
pf_cumul_ret = cumul_ret.mean(axis=1)

# --- Benchmark Data ---
bench_raw = yf.download('^GSPC', start=start)
if 'Adj Close' in bench_raw.columns:
    benchmark = bench_raw['Adj Close']
else:
    st.error("❌ Benchmark data could not be retrieved.")
    st.stop()

bench_ret = benchmark.pct_change()
bench_dev = (bench_ret + 1).cumprod() - 1
bench_risk = bench_ret.std()

# --- Portfolio Risk ---
W = np.ones(len(ret_df.columns)) / len(ret_df.columns)
pf_std = (W.dot(ret_df.cov()).dot(W)) ** 0.5

# --- Chart: Portfolio vs Benchmark ---
st.subheader("📊 Portfolio vs. S&P 500 Performance")
tog = pd.concat([bench_dev, pf_cumul_ret], axis=1)
tog.columns = ['S&P 500 Performance', 'Portfolio Performance']
st.line_chart(tog)

# --- Risk Metrics ---
st.subheader("📉 Portfolio Risk (Volatility)")
st.write(f"Portfolio Standard Deviation: `{pf_std:.4f}`")

st.subheader("📉 Benchmark Risk")
st.write(f"S&P 500 Standard Deviation: `{bench_risk:.4f}`")

# --- Portfolio Composition Pie ---
st.subheader("📌 Portfolio Composition")
fig, ax = plt.subplots(facecolor='#121212')
ax.pie(W, labels=data.columns, autopct='%1.1f%%', textprops={'color': 'white'})
st.pyplot(fig)
