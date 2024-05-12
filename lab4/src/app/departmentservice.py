from typing import List, Protocol

from src.app.model import Department


class DepartmentProvider:

    def get_department_by_id(self, department_id: int) -> Department:
        ...

    def get_departments(self) -> List[Department]:
        ...

    def create_department(self, department: Department) -> None:
        ...

    def update_department(self, department: Department) -> None:
        ...

    def delete_department(self, department_id: int) -> None:
        ...


class DepartmentService:
    _provider: DepartmentProvider
    _models: List[Department]

    def __init__(self, provider: DepartmentProvider) -> None:
        self._provider = provider

    def get_departments(self) -> List[Department]:
        departments = self._provider.get_departments()
        return departments

    def get_department_by_id(self, id: int) -> Department:
        return self._provider.get_department_by_id(id)

    def create_department(self, department: Department) -> None:
        self._provider.create_department(department)

    def update_department(self, new_department_data: Department) -> None:
        model = new_department_data
        self._provider.update_department(model)
