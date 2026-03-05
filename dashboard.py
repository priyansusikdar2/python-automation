import sqlite3
import pandas as pd
import streamlit as st

conn = sqlite3.connect("data/products.db")

df = pd.read_sql_query("SELECT * FROM products", conn)

st.title("Amazon Product Tracker")

st.write("Total Products:", len(df))

st.dataframe(df)

for i,row in df.iterrows():

    st.subheader(row["name"])

    st.write("Price:", row["price"])

    st.write("Rating:", row["rating"])

    st.write("Link:", row["link"])

    if row["image"] != "":
        st.image(row["image"], width=200)