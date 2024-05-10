from typing import Protocol, List

from model.departmentmodel import DepartmentModel


class DepartmentProvider:
    def get_all_departments(self) -> List[DepartmentModel]:
        ...

    def get_department_by_id(self, department_id: int) -> DepartmentModel:
        ...

    def save_department(self, department: DepartmentModel) -> None:
        ...


class DepartmentService:
    _provider: DepartmentProvider
    _model : DepartmentModel

    def __init__(self, provider: DepartmentProvider) -> None:
        self._provider = provider

    def get_departments(self) -> List[DepartmentModel]:
        departments = self._provider.get_all_departments()
        return departments

    def update_department(self, new_department_data: DepartmentModel) -> None:
        model = new_department_data
        self._provider.save_department(model)
