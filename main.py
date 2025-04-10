import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from scipy.optimize import minimize

# Set the title of the Streamlit app
st.title('Portfolio Optimizer & Algorithmic Trading Model')

# Create tabs for the portfolio optimizer and trading algorithm
tabs = st.sidebar.radio("Select a Tab", ["Portfolio Optimizer", "Algorithmic Trading"])

# Portfolio Optimizer Tab
if tabs == "Portfolio Optimizer":
    st.header('Optimize Your Portfolio')

    # Asset input fields (can be a list of tickers)
    tickers = st.text_input('Enter tickers of stocks/bonds (comma separated):', 'AAPL, BND, TSLA')
    tickers = tickers.split(',')

    # Fetch historical data from Yahoo Finance
    data = yf.download(tickers, start="2020-01-01", end="2023-12-31")['Adj Close']

    # Show the data
    st.write("Historical Data:")
    st.dataframe(data)

    # Calculate returns
    returns = data.pct_change().dropna()

    # Portfolio optimization
    def portfolio_volatility(weights, mean_returns, cov_matrix):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    def portfolio_return(weights, mean_returns):
        return np.sum(mean_returns * weights)

    # Optimization function
    def optimize_portfolio(mean_returns, cov_matrix):
        num_assets = len(mean_returns)
        args = (mean_returns, cov_matrix)
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for asset in range(num_assets))
        initial_weights = num_assets * [1. / num_assets]
        opt_results = minimize(portfolio_volatility, initial_weights, args=args, method='SLSQP', bounds=bounds, constraints=constraints)
        return opt_results

    # Calculate mean returns and covariance matrix
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    # Run the optimization
    optimized_result = optimize_portfolio(mean_returns, cov_matrix)
    optimized_weights = optimized_result.x

    # Display optimized portfolio
    st.write("Optimized Portfolio Weights:")
    optimized_portfolio = pd.DataFrame(optimized_weights, index=tickers, columns=["Weight"])
    st.dataframe(optimized_portfolio)

    # Plotting the efficient frontier (Optional)
    num_portfolios = 10000
    results = np.zeros((3, num_portfolios))
    for i in range(num_portfolios):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)
        portfolio_return_val = portfolio_return(weights, mean_returns)
        portfolio_volatility_val = portfolio_volatility(weights, mean_returns, cov_matrix)
        results[0, i] = portfolio_return_val
        results[1, i] = portfolio_volatility_val
        results[2, i] = portfolio_return_val / portfolio_volatility_val

    max_sharpe_idx = np.argmax(results[2])
    max_sharpe_return = results[0, max_sharpe_idx]
    max_sharpe_volatility = results[1, max_sharpe_idx]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=results[1], y=results[0], mode='markers', marker=dict(color=results[2], colorscale='Viridis', size=5)))
    fig.add_trace(go.Scatter(x=[max_sharpe_volatility], y=[max_sharpe_return], mode='markers', marker=dict(color='red', size=12, symbol='star')))
    fig.update_layout(title='Efficient Frontier', xaxis_title='Volatility (Risk)', yaxis_title='Return', showlegend=False)
    st.plotly_chart(fig)

# Algorithmic Trading Model Tab
elif tabs == "Algorithmic Trading":
    st.header('Algorithmic Trading Model for Canadian Government Bonds')

    # Access real-time bond data from Yahoo Finance (using Canadian Government Bond ETFs)
    ticker_bond = st.text_input('Enter Canadian Government Bond ETF Ticker (e.g., XBB.TO):', 'XBB.TO')
    bond_data = yf.download(ticker_bond, start="2020-01-01", end="2023-12-31")

    # Display bond data
    st.write("Bond Data:")
    st.dataframe(bond_data)

    # Trading Strategy Example: Moving Average Crossover
    short_window = 50
    long_window = 200
    bond_data['Short_MA'] = bond_data['Adj Close'].rolling(window=short_window, min_periods=1).mean()
    bond_data['Long_MA'] = bond_data['Adj Close'].rolling(window=long_window, min_periods=1).mean()

    # Trading Signal (1: Buy, -1: Sell, 0: Hold)
    bond_data['Signal'] = 0
    bond_data['Signal'][short_window:] = np.where(bond_data['Short_MA'][short_window:] > bond_data['Long_MA'][short_window:], 1, 0)
    bond_data['Position'] = bond_data['Signal'].diff()

    # Display trading signals
    st.write("Trading Signals:")
    st.dataframe(bond_data[['Adj Close', 'Short_MA', 'Long_MA', 'Signal', 'Position']].tail())

    # Plot the bond price and the moving averages
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=bond_data.index,
                                open=bond_data['Open'], high=bond_data['High'], low=bond_data['Low'], close=bond_data['Adj Close'],
                                name='Candlestick'))
    fig.add_trace(go.Scatter(x=bond_data.index, y=bond_data['Short_MA'], mode='lines', name='50-day MA', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=bond_data.index, y=bond_data['Long_MA'], mode='lines', name='200-day MA', line=dict(color='red')))
    fig.update_layout(title=f'Trading Strategy for {ticker_bond}', xaxis_title='Date', yaxis_title='Price', showlegend=True)
    st.plotly_chart(fig)


