from typing import List
import os

from pyodbc import Row

from src.app.employeeservice import EmployeeProvider
from src.app.model.employee import Employee
from src.app.common.dbconnection import DbConnection


class ClientDbProvider(EmployeeProvider):

    def __init__(self):
        self._conn = DbConnection(os.environ.get('POSTGRES_CONN_STR'))

    def get_employee_by_id(self, client_id: int) -> Employee:
        sql = """
            SELECT 
                client_id,
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
            WHERE employee_id = %s
        """
        params = (sql,)
        result = self._conn.execute(sql, params)
        return self._create_employee(result)[0]

    def create_employee(self, employee: Employee) -> None:
        sql = """
            INSERT INTO employee
                (first_name, last_name, middle_name, birth_date, email, phone,
                 sex, hire_date, job_title_id, department_id, note, image_path)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (employee.first_name, employee.last_name, employee.middle_name, employee.birth_date, employee.email,
                  employee.phone, employee.sex, employee.hire_date, employee.job_title_id, employee.department_id,
                  employee.note, employee.image_path)
        self._conn.execute(sql, params)

    def update_employee(self, employee: Employee) -> None:
        sql = """
            UPDATE employee
            SET 
                first_name = %s,
                last_name = %s,
                middle_name = %s,
                birth_date = %s,
                email = %s,
                phone = %s,
                sex = %s,
                hire_date = %s,
                job_title_id = %s,
                department_id = %s,
                note = %s,
                image_path = %s
            WHERE employee_id = %s
        """
        params = (employee.first_name, employee.last_name, employee.middle_name, employee.birth_date, employee.email,
                  employee.phone, employee.sex, employee.hire_date, employee.job_title_id, employee.department_id,
                  employee.note, employee.image_path, employee.client_id)
        self._conn.execute(sql, params)

    def delete_employee(self, employee_id: int) -> None:
        sql = """
            DELETE FROM employee
            WHERE employee_id = %s
        """
        params = (employee_id,)
        self._conn.execute(sql, params)

    def get_employee_by_department(self, department_id: int) -> List[Employee]:
        sql = """
            SELECT 
                first_name,
                last_name,
                middle_name
            FROM employee
            WHERE department_id = %s
        """
        params = (department_id,)
        result = self._conn.execute(sql, params)
        return self._create_employee(result)

    @staticmethod
    def _create_employee(rows: List[Row]) -> List[Employee]:
        models = []
        for row in rows:
            employee = Employee(
                client_id=row.client_id,
                first_name=row.first_name,
                last_name=row.last_name,
                middle_name=row.middle_name,
                birth_date=row.birth_date,
                email=row.email,
                phone=row.phone,
                sex=row.sex,
                hire_date=row.hire_date,
                job_title_id=row.job_title_id,
                department_id=row.department_id,
                note=row.note,
                image_path=row.image_path
            )
            models.append(employee)
        return models
