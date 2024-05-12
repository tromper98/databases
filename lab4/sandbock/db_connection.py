from src.app.common.dbconnection import DbConnection
conn_str = (
    "DRIVER={PostgreSQL Unicode};"
    "DATABASE=postgres;"
    "UID=admin;"
    "PWD=12345;"
    "SERVER=localhost;"
    "PORT=5432;"
    )
DSN = 'postgresql://admin:12345@postgres-db:5432/postgres'

conn = DbConnection(conn_str)

sql = 'SELECT * FROM department'

result = conn.execute(sql)
pass
row = result[0]
dep_id = row.department_id
pass