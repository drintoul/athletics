import streamlit as st
import mysql.connector

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

pet_owners = conn.query("select * from pet_owners;")

for row in pet_owners.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
