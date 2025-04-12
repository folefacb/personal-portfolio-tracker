import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go


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
    
        # Setup plot
        fig = go.Figure()
    
        # Cumulative portfolio value line
        fig.add_trace(go.Scatter(
            x=df['Time'],
            y=df['Value'],
            mode='lines',
            name='Portfolio Value',
            line=dict(color='#00ffff', width=2.5)
        ))
    
        # Buys
        buys = df[df['Quantity'] > 0]
        fig.add_trace(go.Scatter(
            x=buys['Time'],
            y=buys['Value'],
            mode='markers',
            name='Buy',
            marker=dict(color='limegreen', size=12, symbol='triangle-up'),
            hovertemplate='Buy<br>Time: %{x}<br>Value: %{y}<extra></extra>'
        ))
    
        # Sells
        sells = df[df['Quantity'] < 0]
        fig.add_trace(go.Scatter(
            x=sells['Time'],
            y=sells['Value'],
            mode='markers',
            name='Sell',
            marker=dict(color='crimson', size=12, symbol='triangle-down'),
            hovertemplate='Sell<br>Time: %{x}<br>Value: %{y}<extra></extra>'
        ))
    
        # Layout aesthetics like QuantConnect
        fig.update_layout(
            title='📈 Bond Trading Strategy Backtest',
            xaxis=dict(title='Date', rangeslider=dict(visible=True)),
            yaxis=dict(title='Portfolio Value ($)', fixedrange=False),
            hovermode='x unified',
            template='plotly_dark',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            margin=dict(l=40, r=40, t=60, b=40),
            height=600
        )
    
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

