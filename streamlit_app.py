import streamlit as st
import pandas as pd
import ploty.express as px
#requirements.txt
st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")


df = pd.read_csv('BTC_10_YEAR.csv')
st.dataframe(df.head())

# Create the plot
fig = px.line(bitcoin, x='Date', y='Close', title='Bitcoin Price Over Time', labels={'Close': 'Price (USD)'})

# Display the plot in Streamlit
st.plotly_chart(fig)
