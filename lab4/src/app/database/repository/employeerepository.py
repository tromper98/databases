import os
from typing import List, Optional

from pyodbc import Row

from src.app.database.model.employee import Employee
from src.app.common.dbconnection import DbConnection


class EmployeeRepository:

    def __init__(self):
        self._conn = DbConnection(os.environ.get('POSTGRES_CONN_STR'))

    def find(self, employee_id: int) -> Optional[Employee]:
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
        if len(result) == 0:
            return None
        return self._create_employee(result[0])

    def find_by_department_id(self, department_id) -> Optional[List[Employee]]:
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
        if len(result) == 0:
            return None
        return [self._create_employee(row) for row in result]

    def store(self, employee: Employee) -> None:
        if employee.employee_id:
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
            params = (
                employee.first_name, employee.last_name, employee.middle_name, employee.birth_date, employee.email,
                employee.phone, employee.sex, employee.hire_date, employee.job_title_id, employee.department_id,
                employee.note, employee.image_path, employee.employee_id)
            self._conn.update(sql, params)
        else:
            sql = """
                INSERT INTO employee
                    (first_name, last_name, middle_name, birth_date, email, phone,
                     sex, hire_date, job_title_id, department_id, note, image_path)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            params = (
                employee.first_name, employee.last_name, employee.middle_name, employee.birth_date, employee.email,
                employee.phone, employee.sex, employee.hire_date, employee.job_title_id, employee.department_id,
                employee.note, employee.image_path)
            self._conn.insert(sql, params)

    def remove_by_ids(self, employee_ids: List[int]) -> None:
        sql = f"""
            DELETE FROM employee
            WHERE employee_id IN ({', '.join(['?' for _ in employee_ids])})
        """
        params = tuple(employee_ids)
        self._conn.delete(sql, params)

    def save_employee_image(self, file) -> None:
        file.save()

    @staticmethod
    def _create_employee(row: Row) -> Employee:
        return Employee(
            employee_id=row.employee_id,
            first_name=row.first_name,
            last_name=row.last_name,
            middle_name=row.middle_name,
            birth_date=row.birth_date.date(),
            email=row.email,
            phone=row.phone,
            sex=row.sex,
            hire_date=row.hire_date.date(),
            job_title_id=row.job_title_id,
            department_id=row.department_id,
            note=row.note,
            image_path=row.image_path
        )
