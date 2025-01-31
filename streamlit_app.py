import streamlit as st
import pandas as pd
import plotly.express as px

#requirements.txt
st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")


df = pd.read_csv('BTC_10_YEAR.csv')
st.dataframe(df.head())
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Drop rows with missing values in 'Date' or 'Close'
df = df.dropna(subset=['Date', 'Close'])

# Create the histogram plot
fig = px.histogram(df, x='Date', y='Close', title='Bitcoin Price Over Time', labels={'Close': 'Price (USD)'})

# Show the plot
fig.show()

