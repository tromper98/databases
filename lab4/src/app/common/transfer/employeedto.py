from __future__ import annotations
from typing import Optional
from datetime import date
from dataclasses import dataclass


@dataclass
class EmployeeDTO:
    employee_id: Optional[int]
    first_name: str
    last_name: str
    middle_name: Optional[str]
    birth_date: date
    email: Optional[str]
    phone: Optional[str]
    sex: str
    hire_date: date
    job_title_id: int
    department_id: Optional[int]
    note: str
    image_path: Optional[str]

    @staticmethod
    def from_dict(dt: dict) -> EmployeeDTO:
        if 'employee_id' not in dt.keys():
            employee_id = None
        else:
            employee_id = int(dt['employee_id'])

        if 'image_path' not in dt.keys():
            image_path = None
        else:
            image_path = dt['image_path']

        return EmployeeDTO(
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
