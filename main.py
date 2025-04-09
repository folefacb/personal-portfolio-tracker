import numpy as np 
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

st.title("Investment Portfolio Dashboard")

# Convert input string to a list of tickers
assets_input = st.text_input("Provide your assets (comma-separated)", "AAPL, MSFT, GOOGL")
assets = [ticker.strip().upper() for ticker in assets_input.split(',') if ticker.strip()]

start = st.date_input("Pick a starting date for your analysis", 
                      value=pd.to_datetime('2022-06-01'))

# Download portfolio data safely
data = yf.download(assets, start=start).get('Adj Close')

if data is not None and not data.empty:
    # Calculate portfolio returns
    ret_df = data.pct_change()
    cumul_ret = (ret_df + 1).cumprod() - 1
    pf_cumul_ret = cumul_ret.mean(axis=1)

    # Download benchmark data
    benchmark = yf.download('^GSPC', start=start).get('Adj Close')
    if benchmark is not None and not benchmark.empty:
        bench_ret = benchmark.pct_change()
        bench_dev = (bench_ret + 1).cumprod() - 1
        bench_risk = bench_ret.std()
    else:
        st.warning("Benchmark data could not be retrieved.")
        bench_dev = pd.Series(dtype=float)
        bench_risk = None

    # Portfolio risk calculation
    W = np.ones(len(ret_df.columns)) / len(ret_df.columns)
    pf_std = (W.dot(ret_df.cov()).dot(W)) ** 0.5

    # Portfolio vs Benchmark chart
    st.subheader("Portfolio vs. Index Development")
    tog = pd.concat([bench_dev, pf_cumul_ret], axis=1)
    tog.columns = ['S&P 500 Performance', 'Portfolio Performance']
    st.line_chart(tog)

    # Portfolio risk
    st.subheader("Portfolio Risk:")
    st.write(f"{pf_std:.4f}")

    # Benchmark risk
    st.subheader("Benchmark Risk:")
    st.write(f"{bench_risk:.4f}" if bench_risk else "Unavailable")

    # Portfolio composition
    st.subheader("Portfolio Composition:")
    fig, ax = plt.subplots(facecolor='#121212')
    ax.pie(W, labels=data.columns, autopct='%1.1f%%', textprops={'color': 'white'})
    st.pyplot(fig)
else:
    st.error("Failed to retrieve data. Please check your ticker symbols.")
