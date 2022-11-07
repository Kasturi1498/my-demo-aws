import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="My Streamlit App",
    layout="wide"
)

st.success("Hello World")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)