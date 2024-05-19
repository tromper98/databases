from __future__ import annotations

from typing import Optional, Dict
from dataclasses import dataclass
from datetime import datetime

from pyodbc import Row


@dataclass
class Employee:
    employee_id: Optional[int]
    first_name: str
    last_name: str
    middle_name: Optional[str]
    birth_date: datetime
    email: Optional[str]
    phone: Optional[str]
    sex: str
    hire_date: datetime
    job_title_id: int
    department_id: int
    note: str
    image_path: Optional[str]

    @staticmethod
    def from_dict(dt: Dict) -> Employee:
        if 'employee_id' not in dt.keys():
            employee_id = None
        else:
            employee_id = int(dt['employee_id'])

        if 'image_path' not in dt.keys():
            image_path = None
        else:
            image_path = dt['image_path']

        return Employee(
            employee_id=employee_id,
            first_name=dt['first_name'],
            last_name=dt['last_name'],
            middle_name=dt['middle_name'],
            birth_date=dt['birth_date'],
            email=dt['email'],
            phone=dt['phone'],
            sex=dt['sex'],
            hire_date=dt['hire_date'],
            job_title_id=dt['job_title_id'],
            department_id=dt['department_id'],
            note=dt['note'],
            image_path=image_path
        )

    @staticmethod
    def from_query_result(row: Row) -> Employee:
        return Employee(
            employee_id=row.employee_id,
            first_name=row.first_name,
            last_name=row.last_name,
            middle_name=row.middle_name,
            birth_date=row.birth_date,
            email=row.email,
            phone=row.phone,
            sex=row.sex,
            hire_date=row.hire_date,
            job_title_id=row.job_title_id,
            department_id=row.department_id,
            note=row.note,
            image_path=row.image_path
        )

