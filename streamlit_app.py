import streamlit as st
import pymysql

# Database connection details
host = "http://47.204.128.249"
user = "python"
password = "python"
database = "pets_db"
port = 3306

# Connect to the database
conn = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
cursor = conn.cursor()

# Streamlit app
st.title("MySQL-Streamlit App")

# Example query
query = "select * from pet_owners"
cursor.execute(query)
results = cursor.fetchall()

# Display results in Streamlit
st.write("Results from MySQL:")
for result in results:
    st.write(result)

# Close the database connection
cursor.close()
conn.close()
