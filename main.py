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
    col1, col2 = st.columns([2, 1])  # Wider column for text, smaller for image

    with col1:
        st.title("Hi There! It's me, Bebongnchu!")
        st.markdown("""
        Hi everyone! I am Bebongnchu, and this is my **personal portfolio website**!
        
        Feel free to explore the different sections to learn more about my projects, academic work, and hobbies.
        """)

    with col2:
        st.image(photo_me, use_container_width=True)

    
                

