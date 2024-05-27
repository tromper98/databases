from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class DepartmentDTO:
    department_id: Optional[int]
    city: str
    street: str
    house: str
    employee_count: int

    def __init__(self, city: str, street: str, house: str, department_id: int = None, employee_count: int = 0):
        self.department_id = department_id
        self.city = city
        self.street = street
        self.house = house
        self.employee_count = employee_count

    @staticmethod
    def from_dict(dt: dict) -> DepartmentDTO:
        if 'department_id' in dt.keys():
            department_id = dt['department_id']
        else:
            department_id = None
        return DepartmentDTO(department_id=department_id, city=dt['city'], street=dt['street'], house=dt['house'])
