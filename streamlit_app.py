import streamlit as st

conn = st.experimental_connection('pets_db', type='sql')

pet_owners = conn.query('select * from pet_owners')

for row in pet_owners.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
