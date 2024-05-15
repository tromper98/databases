from typing import Protocol, List

from src.app.model import Employee


class EmployeeProvider:

    def get_employee_by_id(self, employee_id: int) -> Employee:
        ...

    def create_employee(self, client: Employee) -> None:
        ...

    def update_employee(self, client: Employee) -> None:
        ...

    def delete_employee(self, employee_id: int) -> None:
        ...

    def get_employees_by_department(self, department_id: int) -> List[Employee]:
        ...


class EmployeeService:
    _provider: EmployeeProvider
    _client: Employee

    def __init__(self, provider: EmployeeProvider) -> None:
        self._provider = provider

    def update_client_data(self, new_client_data: Employee) -> None:
        self._client = new_client_data
        self._save_client_data()

    def update_client_department(self, new_department_id: int) -> None:
        self._client.department_id = new_department_id
        self._provider.update_employee(self._client)

    def get_employees_from_department(self, department_id: int) -> List[Employee]:
        employees = self._provider.get_employees_by_department(department_id)
        return employees

    def _save_client_data(self) -> None:
        self._provider.update_employee(self._client)
