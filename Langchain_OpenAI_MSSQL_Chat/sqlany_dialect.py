from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy.sql.sqltypes import String, DateTime, NullType
import sqlanydb

class SQLAnyDialect(DefaultDialect):
    name = 'sqlanywhere'
    driver = 'sqlanydb'

    @classmethod
    def dbapi(cls):
        return sqlanydb

    def create_connect_args(self, url):
        opts = url.translate_connect_args(username='user')
        opts.update(url.query)
        return [[], opts]

    def has_table(self, connection, table_name, schema=None):
        query = f"SELECT COUNT(*) FROM SYS.SYSTABLE WHERE table_name = '{table_name}'"
        cursor = connection.execute(query)
        return cursor.fetchone()[0] > 0

    def get_table_names(self, connection, schema=None, **kw):
        query = "SELECT table_name FROM SYS.SYSTABLE"
        cursor = connection.execute(query)
        return [row[0] for row in cursor.fetchall()]

# Other necessary methods and type mappings need to be added here.
