import streamlit as st

@st.data_cache(allow_output_mutation=True)
def get_connection():
    return create_engine("mssql+pyodbc://username:password@DB_server/database?driver=ODBC+Driver+17+for+SQL+Server", 
    fast_executemany = True
    )

@st.data_cache
def read_df(q):
  df = pd.read_sql_query(q, get_connection())
  return df

q1 = 'SELECT * from mytable;'
df = read_df(q1)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
