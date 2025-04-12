import numpy as np 
import pandas as pd
import yfinance as yf
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
                

