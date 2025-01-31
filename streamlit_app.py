import streamlit as st
import pandas as pd
import plotly.express as px

#requirements.txt
st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")


df = pd.read_csv('BTC_10_YEAR.csv')
st.dataframe(df.head())

# Assuming 'df' is your DataFrame
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Sort by 'Date' column and assign it back to 'df'
df = df.sort_values(by='Date')

# Continue with your Plotly or other operations
fig = px.line(df, x='Date', y='Close', title='Bitcoin Price Over Time')


# Display the plot in Streamlit
st.plotly_chart(fig)

