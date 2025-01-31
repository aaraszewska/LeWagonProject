import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Crypto Dashboard", page_icon="💰", layout="wide")

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/home.py", label="🏠 Home")

st.title("Cryptocurrency Price Prediction")
st.write("Welcome to the Crypto Dashboard. Navigate using the sidebar.")


# Sample Data Loading (Uncomment when using real CSV)
# df = pd.read_csv('BTC_10_YEAR.csv')
# df.columns = df.columns.str.strip()  # Clean column names

# Example Plot
# fig = px.histogram(df, x='Date', y='Close', title='Bitcoin Price Over Time', labels={'Close': 'Price (USD)'})
# st.plotly_chart(fig)


