import streamlit as st
import pandas as pd
import plotly.express as px

#requirements.txt
st.title("Cryptocurrency Price Prediction Using ARIMA and Random Forest Models")
import streamlit as st

create_page = st.Page("create.py", title="Create entry", icon=":material/add_circle:")
delete_page = st.Page("delete.py", title="Delete entry", icon=":material/delete:")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()

df = pd.read_csv('BTC_10_YEAR.csv')
st.dataframe(df.head())
df.columns = df.columns.str.strip()  # Strips any leading or trailing spaces


fig = px.histogram(df, x='Date', y='Close', title='Bitcoin Price Over Time', labels={'Close': 'Price (USD)'})

st.plotly_chart(fig)


