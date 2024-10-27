import streamlit as st
import pandas as pd

st.set_page_config(page_title="Our Web Page", layout="wide", initial_sidebar_state="expanded")
st.logo("logo.png")

st.title("Analysis of Data sets")
st.markdown("---")
st.markdown("""
    <style>
        .big-font {
            font-size: 50px;
        }
    </style>
    <p class="big-font"><b>WELCOME!!</b></p>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        .big-font {
            font-size: 20px;
        }
    </style>
    <p class="big-font">This website will help you visualize and analyise you data sets</p>
""", unsafe_allow_html=True)
st.markdown("Please go the navigation bar to select your prefered area")

st.sidebar.title('Navigation Menu:')

st.sidebar.write("[Page 1: Data Overview]")
st.sidebar.write("[Page 2: Insights and Visualizations]")

import page1
import page2
# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Go to", ["Main", "Page 1", "Page 2"])

# Navigation based on selection
if selection == "main":
    st.write("This is the main page.")
elif selection == "Page 1":
    page1.page1()  
elif selection == "Page 2":
    page2.page2()





