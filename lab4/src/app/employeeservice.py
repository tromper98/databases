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

    def is_employee_exists(self, employee_id: int) -> bool:
        ...

    def get_employees_by_department(self, department_id: int) -> List[Employee]:
        ...


class EmployeeService:
    _provider: EmployeeProvider

    def __init__(self, provider: EmployeeProvider) -> None:
        self._provider = provider

    def update_client_department(self, new_department_id: int) -> None:
        self._client.department_id = new_department_id
        self._provider.update_employee(self._client)

    def get_employees_from_department(self, department_id: int) -> List[Employee]:
        employees = self._provider.get_employees_by_department(department_id)
        return employees

    def remove_employee_from_department(self, employee_id: int) -> None:
        employee = self.get_employee(employee_id)
        employee.department_id = None
        self._save_employee(employee)

    def get_employee(self, employee_id: int) -> Employee:
        if self._provider.is_employee_exists(employee_id):
            return self._provider.get_employee_by_id(employee_id)
        else:
            raise ValueError(f'Cannot Find employee with employee_id = {employee_id}')

    def _save_employee(self, employee: Employee) -> None:
        self._provider.update_employee(employee)
