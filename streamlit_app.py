import streamlit as st
import pandas as pd
import ploty.express as px
#requirements.txt
st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")


df = pd.read_csv('BTC_10_YEAR.csv')
st.dataframe(df.head())




# Sample dataframe: Replace with your actual dataframe
bitcoin = pd.DataFrame(df)


# Convert 'Date' column to datetime format
bitcoin['Date'] = pd.to_datetime(bitcoin['Date'])

# Sort by date to ensure correct time series visualization
bitcoin = bitcoin.sort_values(by='Date')

# Create the plot
fig = px.line(bitcoin, x='Date', y='Close', title='Bitcoin Price Over Time', labels={'Close': 'Price (USD)'})

# Display the plot in Streamlit
st.plotly_chart(fig)
