from __future__ import annotations

from typing import Dict, Optional

from src.app.common.transfer.departmentdto import DepartmentDTO

# TODO
# 1. Модель не должна хранить те, данные, которые она не
# 2. Превратить DTO в модель Department, реализовать операции обновления состояния модели в классе


class Department(object):
    department_id: Optional[int]
    city: str
    street: str
    house: str

    def __init__(self, city: str, street: str, house: str, department_id: Optional[int] = None) -> None:
        self.department_id = department_id
        self.city = city
        self.street = street
        self.house = house

    def edit(self, department_dto: DepartmentDTO) -> None:
        self.city = department_dto.city
        self.street = department_dto.street
        self.house = department_dto.house
