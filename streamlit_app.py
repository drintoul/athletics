import streamlit as st

conn = st.connection('mysql', type='sql')

df = conn.query('SELECT * FROM mytable;', ttl=600)

for row in df.itertuples():
  st.write(f"{row.name} has a :{row.pet}:")
