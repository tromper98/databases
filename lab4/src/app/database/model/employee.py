from __future__ import annotations

from typing import Optional
from dataclasses import dataclass
from datetime import date

from src.app.common.transfer.employeedto import EmployeeDTO


@dataclass
class Employee:
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
    department_id: int
    note: Optional[str]
    image_path: Optional[str]

    def __init__(self, first_name: str, last_name: str, middle_name: str, birth_date: date, email: str,
                 phone: str, sex: str, hire_date: date, job_title_id: int, department_id: int, note: Optional[str] = None,
                 image_path: str = None, employee_id: Optional[int] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.email = email
        self.phone = phone
        self.sex = sex
        self.hire_date = hire_date
        self.job_title_id = job_title_id
        self.department_id = department_id
        self.note = note
        self.image_path = image_path
        self.employee_id = employee_id

    def edit(self, employee_dto: EmployeeDTO) -> None:
        self.first_name = employee_dto.first_name
        self.last_name = employee_dto.last_name
        self.middle_name = employee_dto.middle_name
        self.birth_date = employee_dto.birth_date
        self.email = employee_dto.email
        self.phone = employee_dto.phone
        self.sex = employee_dto.sex
        self.hire_date = employee_dto.hire_date
        self.job_title_id = employee_dto.job_title_id
        self.department_id = employee_dto.department_id
        self.note = employee_dto.note
        self.image_path = employee_dto.image_path

    @staticmethod
    def from_dto(dto: EmployeeDTO) -> Employee:
        return Employee(
            first_name=dto.first_name,
            last_name=dto.last_name,
            middle_name=dto.middle_name,
            birth_date=dto.birth_date,
            email=dto.email,
            phone=dto.phone,
            sex=dto.sex,
            hire_date=dto.hire_date,
            job_title_id=dto.job_title_id,
            department_id=dto.department_id,
            note=dto.note,
            image_path=dto.image_path
        )
