from typing import Optional, List, Tuple
from contextlib import contextmanager

import pyodbc


class DbConnection:
    _conn_str: str
    _connection: pyodbc.Connection

    def __init__(self, conn_str: str):
        self._conn_str = conn_str

    def select(self, sql, params: Optional[Tuple] = None) -> List[pyodbc.Row]:
        with self.connect_to_db():
            cursor = self._connection.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchall()

    def update(self, sql: str, params: Tuple) -> int:
        with self.connect_to_db():
            cursor = self._connection.cursor()
            cursor.execute(sql, params)
            return cursor.rowcount

    def insert(self, sql: str, params: Tuple) -> int:
        with self.connect_to_db():
            cursor = self._connection.cursor()
            cursor.execute(sql, params)
            return cursor.rowcount

    def delete(self, sql: str, params: Tuple) -> int:
        with self.connect_to_db():
            cursor = self._connection.cursor()
            cursor.execute(sql, params)
            return cursor.rowcount

    def execute(self, sql: str) -> None:
        with self.connect_to_db():
            cursor = self._connection.cursor()
            cursor.execute(sql)

    @contextmanager
    def connect_to_db(self):
        self._connection = pyodbc.connect(self._conn_str, autocommit=True)
        yield
        self._connection.close()
