import pandas as pd 
import streamlit as st

st.markdown("<h1 style= text-align:center;color:cyan;>Data Intro</h1>", unsafe_allow_html=True)

st.set_page_config(page_title="Home" ,layout="wide")

df = pd.read_csv("ai_job_cleaned.csv")
st.divider()
st.dataframe(df.head(10))