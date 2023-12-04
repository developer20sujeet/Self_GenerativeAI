import sqlanydb


DATABASE_SERVER = 'sqldemo'
DATABASE_NAME = 'demo'
DATABASE_USERNAME = 'dba'
DATABASE_PASSWORD = 'sql'
DRIVER = '{SQL Anywhere 17}'

conn = sqlanydb.connect(uid='dba', pwd='sql', eng='sqldemo', dbn='demo' )
curs = conn.cursor()
curs.execute("select 'Hello, world!'")
print( "SQL Anywhere says: %s" % curs.fetchone() )
curs.close()
conn.close()
