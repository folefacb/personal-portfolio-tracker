import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

# Set the title of the Streamlit app
st.title('Stock Dashboard')

# Sidebar for user inputs
ticker = st.sidebar.text_input('Ticker', 'AAPL')  # Default to 'AAPL' if empty
start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2020-01-01'))
end_date = st.sidebar.date_input('End Date', pd.to_datetime('today'))

# Download stock data from Yahoo Finance
if ticker:
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if not data.empty:
            # Create a plot using Plotly
            fig = px.line(data, x=data.index, y=data['Adj Close'], title=f'{ticker} Stock Price')
            st.plotly_chart(fig)
        else:
            st.error(f"No data found for ticker: {ticker}")
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {str(e)}")
else:
    st.warning("Please enter a valid ticker symbol.")



