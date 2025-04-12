import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

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

        # Portfolio Value Line (Use Streamlit's line_chart for continuous line)
        st.subheader("Buy and Sell Signal Graph")

        # Buys and Sells
        buys = df[df['Quantity'] > 0]
        sells = df[df['Quantity'] < 0]

        # Connect buys and sells with a continuous line
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plot the portfolio value (just the continuous line of the portfolio)
        ax.plot(df['Time'], df['Value'], label='Portfolio Value', color='lightblue', alpha=0.7)

        # Plot Buy signals
        ax.scatter(buys['Time'], buys['Value'], color='green', label='Buy Signal', marker='^', s=100)

        # Plot Sell signals
        ax.scatter(sells['Time'], sells['Value'], color='red', label='Sell Signal', marker='v', s=100)

        # Titles and Labels
        ax.set_title('📈 Bond Trading Strategy Backtest with Buy/Sell Signals', fontsize=14)
        ax.set_xlabel('Date')
        ax.set_ylabel('Portfolio Value ($)')
        ax.legend(loc='upper left')
        ax.grid(True)

        st.pyplot(fig)

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
