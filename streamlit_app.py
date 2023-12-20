import streamlit as st
import pymysql
import toml

# Load configuration from config.toml file
config = toml.load("config.toml")
db_config = config["database"]

# Database connection details
host = db_config["host"]
user = db_config["user"]
password = db_config["password"]
database = db_config["name"]
port = db_config["port"]

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

