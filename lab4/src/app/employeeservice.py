from typing import List
from datetime import datetime

from src.app.model import Employee


class EmployeeProvider:

    def get_employee_by_id(self, employee_id: int) -> Employee:
        ...

    def create_employee(self, employee: Employee) -> None:
        ...

    def update_employee(self, employee: Employee) -> None:
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

    def get_employees_from_department(self, department_id: int) -> List[Employee]:
        employees = self._provider.get_employees_by_department(department_id)
        return employees

    def remove_employee_from_department(self, employee_id: int) -> None:
        employee = self.get_employee(employee_id)
        employee.department_id = None
        self._save_employee(employee)

    def get_employee(self, employee_id: int) -> Employee:
        if self._provider.is_employee_exists(employee_id):
            employee = self._provider.get_employee_by_id(employee_id)
            employee.hire_date = employee.hire_date.date()
            employee.birth_date = employee.birth_date.date()
            return employee
        else:
            raise ValueError(f'Cannot Find employee with employee_id = {employee_id}')

    def create_employee(self, employee: Employee) -> None:
        self._provider.create_employee(employee)

    def update_employee(self, new_employee_data: Employee) -> None:
        if self._provider.is_employee_exists(new_employee_data.employee_id):
            self._provider.update_employee(new_employee_data)
        else:
            raise ValueError(f'Cannot update employee with employee_id = {new_employee_data.employee_id} '
                             f'because it does not exists')

    def delete_employee(self, employee_id: int) -> None:
        if self._provider.is_employee_exists(employee_id):
            self._provider.delete_employee(employee_id)
        else:
            raise ValueError(f'Cannot delete employee because with employee_id = {employee_id} '
                             f'because it does not exists')

    def _save_employee(self, employee: Employee) -> None:
        self._provider.update_employee(employee)
