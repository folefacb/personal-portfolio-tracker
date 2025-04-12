import numpy as np 
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

# Use raw string for Windows file path
photo_me = r"Bebongnchu's Projects/BCP_Bebongnchu (2).jpg"

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Research/Thesis", "Hobbies and Interests"])

if page == "Home":
    st.title("Hi There! It's me, Bebongnchu!")
    st.image(photo_me)
    st.markdown("""
    Hi everyone! I am Bebongnchu, and this is my **personal portfolio website**!
    
    Feel free to explore the different sections to learn more about my projects, academic work, and hobbies.
    """)

    
                

