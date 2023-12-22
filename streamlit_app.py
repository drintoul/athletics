import streamlit as st
import pymysql

# Database connection details
host = st.secrets["database"]["host"]
user = st.secrets["database"]["user"]
password = st.secrets["database"]["password"]
database = st.secrets["database"]["name"]
port = st.secrets["database"]["port"]

# Connect to the database
cnxn = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
cursor = cnxn.cursor()

# Streamlit app
st.title("MySQL-Streamlit App")

# Example query
query = "SELECT * FROM pet_owners LIMIT 5"
@st.cache_data(ttl=3600*6)
cursor.execute(query)
results = cursor.fetchall()

# Display results in Streamlit
st.write("Results from MySQL:")
for row in results:
  st.write(row[0], f":{row[1]}:")

# Close the database connection
cursor.close()
cnxn.close()

