import streamlit as st

st.sidebar.page_link("pages/home.py", label="🏠 Home")  # No need for "crypto_app/" in the path



st.title("Cryptocurrency Dashboard")

# Display an image
st.image("sarima.png", caption="Cryptocurrency Logo", use_column_width=True)




