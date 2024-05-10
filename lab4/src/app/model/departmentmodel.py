from dataclasses import dataclass


@dataclass
class DepartmentModel:
    department_id: int
    city: str
    street: str
    house: str
