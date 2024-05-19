from typing import List
import os

from pyodbc import Row

from src.app.employeeservice import EmployeeProvider
from src.app.model.employee import Employee
from src.app.common.dbconnection import DbConnection


class EmployeeDBProvider(EmployeeProvider):

    def __init__(self):
        self._conn = DbConnection(os.environ.get('POSTGRES_CONN_STR'))

    def get_employee_by_id(self, employee_id: int) -> Employee:
        sql = """
            SELECT 
                employee_id,
                first_name,
                last_name,
                middle_name,
                birth_date,
                email,
                phone,
                sex,
                hire_date,
                job_title_id,
                department_id,
                note,
                image_path
            FROM employee
            WHERE employee_id = ?
        """
        params = (employee_id,)
        result = self._conn.select(sql, params)
        return Employee.from_query_result(result[0])

    def create_employee(self, employee: Employee) -> None:
        sql = """
            INSERT INTO employee
                (first_name, last_name, middle_name, birth_date, email, phone,
                 sex, hire_date, job_title_id, department_id, note, image_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (employee.first_name, employee.last_name, employee.middle_name, employee.birth_date, employee.email,
                  employee.phone, employee.sex, employee.hire_date, employee.job_title_id, employee.department_id,
                  employee.note, employee.image_path)
        self._conn.insert(sql, params)

    def update_employee(self, employee: Employee) -> None:
        sql = """
            UPDATE employee
            SET 
                first_name = ?,
                last_name = ?,
                middle_name = ?,
                birth_date = ?,
                email = ?,
                phone = ?,
                sex = ?,
                hire_date = ?,
                job_title_id = ?,
                department_id = ?,
                note = ?,
                image_path = ?
            WHERE employee_id = ?
        """
        params = (employee.first_name, employee.last_name, employee.middle_name, employee.birth_date, employee.email,
                  employee.phone, employee.sex, employee.hire_date, employee.job_title_id, employee.department_id,
                  employee.note, employee.image_path, employee.employee_id)
        self._conn.update(sql, params)

    def delete_employee(self, employee_id: int) -> None:
        sql = """
            DELETE FROM employee
            WHERE employee_id = ?
        """
        params = (employee_id,)
        self._conn.delete(sql, params)

    def get_employees_by_department(self, department_id: int) -> List[Employee]:
        sql = """
            SELECT 
                employee_id,
                first_name,
                last_name,
                middle_name,
                birth_date,
                email,
                phone,
                sex,
                hire_date,
                job_title_id,
                department_id,
                note,
                image_path
            FROM employee
            WHERE department_id = ?
        """
        params = (department_id,)
        result = self._conn.select(sql, params)
        return [Employee.from_query_result(row) for row in result]

    def is_employee_exists(self, employee_id: int) -> bool:
        sql = """
            SELECT 
                1
            FROM employee
            WHERE employee_id = ?
        """
        params = (employee_id,)
        result = self._conn.select(sql, params)
        if result is not None:
            return True
        return False
