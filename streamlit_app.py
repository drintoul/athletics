import streamlit as st
import mysql.connector

@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

@st.cache_data(ttl=600)
pet_owners = conn.query("select * from pet_owners;")

for row in pet_owners.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
