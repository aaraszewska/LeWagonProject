import streamlit as st
import pandas as pd
import plotly.express as px

#requirements.txt
st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")


df = pd.read_csv('BTC_10_YEAR.csv')
st.dataframe(df.head())


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Sort by date to ensure correct time series visualization
pd = pd.sort_values(by='Date')
fig = px.histogram(df,  x='Date', y='Close', title='Bitcoin Price Over Time', labels={'Close': 'Price (USD)'})

# Display the plot in Streamlit
st.plotly_chart(fig)

