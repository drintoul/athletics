import streamlit as st
import pymysql
import toml

# Database connection details
host = st.secrets["host"]
user = st.secrets["user"]
password = st.secrets["password"]
database = st.secrets["name"]
port = st.secrets["port"]

# Connect to the database
conn = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
cursor = conn.cursor()

# Streamlit app
st.title("MySQL-Streamlit App")

# Example query
query = "SELECT * FROM pet_owners LIMIT 5"
cursor.execute(query)
results = cursor.fetchall()

# Display results in Streamlit
st.write("Results from MySQL:")
for result in results:
    st.write(result)

# Close the database connection
cursor.close()
conn.close()

