# import sqlanydb


# DATABASE_SERVER = 'sqldemo'
# DATABASE_NAME = 'demo'
# DATABASE_USERNAME = 'dba'
# DATABASE_PASSWORD = 'sql'
# DRIVER = '{SQL Anywhere 17}'

# conn = sqlanydb.connect(uid='dba', pwd='sql', eng='sqldemo', dbn='demo' )
# curs = conn.cursor()
# curs.execute("select 'Hello, world!'")
# print( "SQL Anywhere says: %s" % curs.fetchone() )
# curs.close()
# conn.close()


#================================https://github.com/langchain-ai/langchain/issues/3645=====================================================

# from sqlalchemy import create_engine

# engine = create_engine("postgresql+psycopg2://{user}:{passwd}@{host}:{port}/chatdatabase")

# with engine.connect() as con:

#   rs = con.execute('select * from table_1 limit 10')
#   for row in rs:
#     print(row)

#=======================================================
import pyodbc

DSN_NAME = 'sql2023'  # Replace with your actual User DSN name

try:
    conn = pyodbc.connect(f'DSN={DSN_NAME}')
    print("Connected successfully")
    # Perform any test query
    conn.close()
except Exception as e:
    print("Error occurred:", e)
