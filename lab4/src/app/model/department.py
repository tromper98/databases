from __future__ import annotations

from typing import Dict, Optional
from dataclasses import dataclass, asdict

from pyodbc import Row


@dataclass
class Department:
    department_id: Optional[int]
    city: str
    street: str
    house: str
    employee_count: Optional[int] = None

    def to_dict(self) -> Dict:
        return {k: str(v) for k, v in asdict(self).items()}

    @staticmethod
    def from_dict(dt: Dict) -> Department:
        if 'department_id' in dt.keys():
            department_id = dt['department_id']
        else:
            department_id = None
        return Department(department_id=department_id, city=dt['city'], street=dt['street'], house=dt['house'])

    @staticmethod
    def from_query_result(row: Row) -> Department:
        return Department(
            department_id=row.department_id,
            city=row.city,
            street=row.street,
            house=row.house,
            employee_count=row.employee_count
        )