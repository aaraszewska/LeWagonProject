import streamlit as st

st.set_page_config(page_title="Crypto Dashboard", page_icon="💰", layout="wide")

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/home.py", label="🏠 Home")

st.title("Cryptocurrency Price Prediction")
st.write("Welcome to the Crypto Dashboard. Navigate using the sidebar.")




st.sidebar.page_link("crypto_app/pages/home.py", label="🏠 Home")
