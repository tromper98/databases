import os
from typing import List

from src.app.database.model import JobTitle
from src.app.common.dbconnection import DbConnection


class JobTitleDBProvider:
    _conn: DbConnection

    def __init__(self):
        self._conn = DbConnection(os.environ.get('POSTGRES_CONN_STR'))

    def find_all(self) -> List[JobTitle]:
        sql = """
            SELECT 
                job_title_id,
                name
            FROM job_title
        """
        result = self._conn.select(sql)
        return [JobTitle.from_query_result(row) for row in result]
