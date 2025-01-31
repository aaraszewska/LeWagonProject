import streamlit as st
import pandas as pd
#requirements.txt
st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")


df = pd.read_csv('BTC_10_YEAR')
st.dataframe(df.head())
