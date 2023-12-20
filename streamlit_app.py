import streamlit as st
import pymysql
import toml

# Database connection details
host = st.secrets["database"]["host"]
user = st.secrets["database"]["user"]
password = st.secrets["database"]["password"]
database = st.secrets["database"]["name"]
port = st.secrets["database"]["port"]

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
for row in results.itertuples():
    st.write(f"{row.owner} has a :{row.pet}:")

# Close the database connection
cursor.close()
conn.close()

