import streamlit as st
import pandas as pd
import numpy as np

# App Configuration and Styling
st.set_page_config(
    page_title="Data Insights App",
    page_icon="📊",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
selected = st.sidebar.radio(
    "Go to:",
    ["Home", "Dataset", "Visualization", "About"]
)

# Initialize Session State for Dataset
def initialize_session_state():
    if "uploaded_file" not in st.session_state:
        st.session_state["uploaded_file"] = None
    if "df" not in st.session_state:
        st.session_state["df"] = None
initialize_session_state()

# Header Section
st.title("📊 Data Insights App")
st.markdown("### Analyze and visualize your data effortlessly!")

# Home Section
if selected == "Home":
    st.header("Welcome to the Data Insights App")
    st.markdown(
        """
        This app helps you explore, visualize, and gain insights from your data. 
        Use the navigation menu to get started:
        - **Dataset**: Upload and preview your dataset.
        - **Visualization**: Create interactive charts.
        - **About**: Learn more about this app.
        """
    )

# Dataset Section
elif selected == "Dataset":
    st.header("📂 Upload and Explore Your Dataset")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.session_state["uploaded_file"] = uploaded_file
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df
        st.success("File uploaded successfully!")
        st.subheader("Dataset Preview")
        st.write(df.head())
        
        st.subheader("Dataset Summary")
        st.write(df.describe())
    else:
        st.info("Please upload a CSV file to get started.")

# Visualization Section

elif selected == "Visualization":
    st.header("📈 Create Visualizations")
    st.markdown("Choose columns to create a bar chart.")

    if st.session_state["df"] is not None:
        df = st.session_state["df"]
        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("Select X-axis column:", df.columns)
        with col2:
            y_axis = st.selectbox("Select Y-axis column:", df.columns)

        if st.button("Generate Chart"):
            st.subheader("Bar Chart Visualization")
            # Using Plotly for better visualization
            import plotly.express as px
            fig = px.bar(df, x=x_axis, y=y_axis, title="Bar Chart", labels={x_axis: x_axis, y_axis: y_axis})
            st.plotly_chart(fig)
    else:
        st.warning("Upload a dataset first in the Dataset section.")


# About Section
elif selected == "About":
    st.header("ℹ️ About this App")
    st.markdown(
        """
        **Data Insights App** is built with Streamlit to provide an easy-to-use platform for exploring datasets 
        and creating visualizations. 

        - **Developer**: **SABIHA SULTANA**
        - **GitHub**: [https://github.com/SabihaSultanaa/Growth-Mindset-Challenge.git]
     
        """
    )


