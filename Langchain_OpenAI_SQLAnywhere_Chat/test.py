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
# import pyodbc

# DSN_NAME = 'sql2023'  # Replace with your actual User DSN name

# try:
#     conn = pyodbc.connect(f'DSN={DSN_NAME}')
#     print("Connected successfully")
#     # Perform any test query
#     conn.close()
# except Exception as e:
#     print("Error occurred:", e)

#==================================
# import sys

# for path in sys.path:
#     if "sqlalchemy_sqlany" in path:
#         print(f"Found sqlalchemy_sqlany in: {path}")

# import sqlalchemy

# #print("sqlalchemy imported successfully!")

# import sqlalchemy_sqlany

# # Check if sqlalchemy_sqlany dialect is registered with SQLAlchemy
# print(sqlalchemy.dialects.registry.available())



# from sqlalchemy import create_engine

# try:
#     # Replace 'your_dialect' with the name of the dialect you're checking
#     engine = create_engine('sqlalchemy_sqlany://')
#     print("Dialect is registered.")
# except ImportError:
#     print("Dialect is not registered.")


# from sqlalchemy.dialects import registry

# # List all registered dialect names
# print(registry.keys())

# # Check if a specific dialect is registered
# if 'your_dialect' in registry:
#     print("Dialect is registered.")
# else:
#     print("Dialect is not registered.")









from sqlalchemy.dialects import registry
registry.register('sqlalchemy_sqlany', 'sqlalchemy_sqlany.base', 'SQLAnyDialect')

from sqlalchemy.testing import runner

runner.main()
