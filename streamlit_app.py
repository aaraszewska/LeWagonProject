import streamlit as st
import pandas as pd
import plotly.express as px

#requirements.txt
st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")


df = pd.read_csv('BTC_10_YEAR.csv')
st.dataframe(df.head())
df.columns = df.columns.str.strip()  # Strips any leading or trailing spaces


fig = px.histogram(df, x='Date', y='Close', title='Bitcoin Price Over Time', labels={'Close': 'Price (USD)'})

st.plotly_chart(fig)


