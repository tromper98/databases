from typing import Optional, List, Tuple
from contextlib import contextmanager

import pyodbc


class DbConnection:
    _conn_str: str
    _connection: pyodbc.Connection

    def __init__(self, conn_str: str):
        self._conn_str = conn_str

    def execute(self, sql, params: Optional[Tuple] = None) -> Optional[List[pyodbc.Row]]:
        with self.connect_to_db():
            cursor = self._connection.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchall()

    @contextmanager
    def connect_to_db(self):
        self._connection = pyodbc.connect(self._conn_str, autocommit=True)
        yield
        self._connection.close()
