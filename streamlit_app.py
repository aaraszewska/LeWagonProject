import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Manager", page_icon="✏️")

st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/create.py", label="Create Entry", icon="➕")
st.sidebar.page_link("pages/delete.py", label="Delete Entry", icon="🗑️")

# Sample Data Loading (Uncomment when using real CSV)
# df = pd.read_csv('BTC_10_YEAR.csv')
# df.columns = df.columns.str.strip()  # Clean column names

# Example Plot
# fig = px.histogram(df, x='Date', y='Close', title='Bitcoin Price Over Time', labels={'Close': 'Price (USD)'})
# st.plotly_chart(fig)


