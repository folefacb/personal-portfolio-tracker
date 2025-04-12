import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
import technical_analysis 
import Indicators  # Fixed import for technical-analysis package

# Use raw string for Windows/Linux-friendly relative path
photo_me = r"Bebongnchu's Projects/BCP_Bebongnchu (2).jpg"

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Research/Thesis", "Hobbies and Interests"])

if page == "Home":
    col1, col2 = st.columns([2, 1.5])  # Wider column for text, smaller for image

    with col1:
        st.title("Welcome to my personal portfolio!")
        st.markdown("""Hi! My name is Bebongnchu, and I’m a third-year Mathematics and Finance student at McMaster University with a strong passion for finance and technology.

I'm always exploring the integration and intersection of both fields through hands-on projects and personal initiatives.

Here, you can learn more about my portfolio, academic journey, and even a few of my personal interests. Enjoy!""")

    with col2:
        st.image(photo_me, use_container_width=True)
    st.markdown("---")  # horizontal line for separation

    # Dashboard-style LinkedIn button
    st.subheader("Connect with me")

    col3, col4 = st.columns([0.1, 0.9])

    with col3:
        st.image("Link.png", width=30)

    with col4:
        st.markdown(
            "[LinkedIn](https://www.linkedin.com/in/bebongnchu-folefac-5ab894268/)",
            unsafe_allow_html=True
        )

    col3, col4 = st.columns([0.1, 0.9])
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/25/25231.png", width=30)
    with col4:
        st.markdown(
            "[GitHub](https://github.com/folefacb)",
            unsafe_allow_html=True
        )
    col3, col4 = st.columns([0.1, 0.9])
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=30)  # resume icon
    with col4:
        st.markdown(
            "[View My Resume](file:///C:/Users/bebon/Downloads/resume%20(43).pdf)",
            unsafe_allow_html=True
        )

if page == "Projects":
    tab1, tab2, tab3 = st.tabs(["📈 Bond Trading Algorithm", "📊 Data Display Dashboard", "♟️ Chess AI Bot"])

    with tab1:
        st.header("Bond Trading Algorithm")
        st.markdown("""
        This project involves an automated bond trading algorithm using QuantConnect.  
        It utilizes indicators like moving averages and implements position sizing, stop-loss, and take-profit strategies.  
        Designed for risk-adjusted returns and market efficiency.
        """)
        st.markdown("[🔗 View on GitHub](https://github.com/your-username/bond-trading-algorithm)")
    
        # Load the trade file
        uploaded_file = r"Determined Yellow Dinosaur_trades.csv"
        df = pd.read_csv(uploaded_file)
    
        # Preprocessing
        df['Time'] = pd.to_datetime(df['Time'])
        df = df.sort_values('Time')

        # Technical analysis using the technical-analysis package
        indicators = Indicators(df)
        df['SMA'] = indicators.sma(window=14)  # Simple Moving Average (14 periods)

        # Generate Buy/Sell signals based on price crossing SMA
        df['Buy Signal'] = (df['Close'] > df['SMA']) & (df['Close'].shift(1) <= df['SMA'].shift(1))
        df['Sell Signal'] = (df['Close'] < df['SMA']) & (df['Close'].shift(1) >= df['SMA'].shift(1))

        # Create a Plotly figure
        fig = go.Figure()

        # Add Candlestick Chart
        fig.add_trace(go.Candlestick(
            x=df['Time'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='Candlesticks',
            increasing_line_color='green', decreasing_line_color='red'
        ))

        # Add Buy signals
        buy_signals = df[df['Buy Signal'] == True]
        fig.add_trace(go.Scatter(
            x=buy_signals['Time'],
            y=buy_signals['Close'],
            mode='markers',
            name='Buy Signal',
            marker=dict(color='lime', size=10, symbol='triangle-up'),
            hovertemplate='Buy<br>Time: %{x}<br>Value: %{y}<extra></extra>'
        ))

        # Add Sell signals
        sell_signals = df[df['Sell Signal'] == True]
        fig.add_trace(go.Scatter(
            x=sell_signals['Time'],
            y=sell_signals['Close'],
            mode='markers',
            name='Sell Signal',
            marker=dict(color='crimson', size=10, symbol='triangle-down'),
            hovertemplate='Sell<br>Time: %{x}<br>Value: %{y}<extra></extra>'
        ))

        # Layout customization
        fig.update_layout(
            title='📈 Bond Trading Strategy with Buy/Sell Signals',
            xaxis_title='Date',
            yaxis_title='Portfolio Value ($)',
            xaxis_rangeslider_visible=False,
            template='plotly_dark',
            height=600,
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
        )

        # Display the plot in Streamlit
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.header("Data Display Dashboard")
        st.markdown("""
        A sleek, interactive data visualization dashboard built with Streamlit and Plotly.  
        It allows users to explore stock prices, custom filters, and generate insights from uploaded datasets.
        """)
        st.markdown("[🔗 View on GitHub](https://github.com/your-username/data-dashboard)")

    with tab3:
        st.header("Chess AI Machine Learning Bot")
        st.markdown("""
        This AI bot was trained to play chess using reinforcement learning and neural networks.  
        The model learns from thousands of simulated games and improves over time by evaluating board positions.
        """)
        st.markdown("[🔗 View on GitHub](https://github.com/your-username/chess-ai-bot)")

