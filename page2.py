import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page2():
    st.title("Plot Generator")
    
    file_uploader = st.file_uploader("Upload your CSV file", type=["csv","tsv","xls","xlsx"])

    x_axis = st.text_input("Enter the x-axis column name")
    y_axis = st.text_input("Enter the y-axis column name")

    plot_type = st.selectbox("Select the plot type", ["Line Plot", "Scatter Plot", "Bar Plot", "Histogram"])

    generate_plot = st.button("Generate Plot")

    if file_uploader is not None:
        df = pd.read_csv(file_uploader)
        st.write("Preview of the dataset:")
        st.write(df.head())
    if generate_plot:
        if plot_type == "Line Plot":
            fig, ax = plt.subplots()
            ax.plot(df[x_axis], df[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title("Line Plot")
            st.pyplot(fig)
        elif plot_type == "Scatter Plot":
            fig, ax = plt.subplots()
            ax.scatter(df[x_axis], df[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title("Scatter Plot")
            st.pyplot(fig)
        elif plot_type == "Bar Plot":
            fig, ax = plt.subplots()
            ax.bar(df[x_axis], df[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title("Bar Plot")
            st.pyplot(fig)
        elif plot_type == "Histogram":
            fig, ax = plt.subplots()
            ax.hist(df[y_axis], bins=50)
            ax.set_xlabel(y_axis)
            ax.set_ylabel("Frequency")
            ax.set_title("Histogram")
            st.pyplot(fig)
        
