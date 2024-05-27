from __future__ import annotations

from dataclasses import dataclass

from pyodbc import Row


@dataclass
class JobTitle:
    job_title_id: int
    name: str

    @staticmethod
    def from_query_result(row: Row) -> JobTitle:
        return JobTitle(job_title_id=row.job_title_id, name=row.name)
