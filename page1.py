import streamlit as st
import pandas as pd
def page1():
    st.title('Data Overview')
    file_uploader = st.file_uploader("Upload your CSV file", type=["csv","tsv","xls","xlsx"])
    if file_uploader is not None:
        df = pd.read_csv(file_uploader)
        st.write("Here is a preview of the dataset:")
        st.write(df.head())
        st.write("Dataset statistics:")
        st.write(df.describe())
        st.subheader("Data Types")
        st.write(df.dtypes) 
        st.subheader("Missing Values")
        st.write(df.isnull().sum()) 
        st.subheader("Unique Values")
        st.write(df.nunique())
        st.subheader("Data Overview")
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")



