from typing import List
import os

from pyodbc import Row
from src.app.departmentservice import DepartmentProvider
from src.app.model.department import Department
from src.app.common.dbconnection import DbConnection


class DepartmentDBProvider(DepartmentProvider):

    def __init__(self):
        self._conn = DbConnection(os.environ.get('POSTGRES_CONN_STR'))

    def get_department_by_id(self, department_id: int) -> Department:
        sql = """
            SELECT 
                d.department_id,
                d.city,
                d.street,
                d.house,
                COUNT(DISTINCT e.employee_id) AS employee_count
            FROM department d
                LEFT JOIN employee e ON d.department_id = e.department_id
            WHERE d.department_id = ?
            GROUP BY
                d.department_id,
                d.city,
                d.street,
                d.house
        """
        params = (department_id,)
        result = self._conn.execute(sql, params)
        return self._create_departments(result)[0]

    def get_departments(self) -> List[Department]:
        sql = """
            SELECT 
                d.department_id,
                d.city,
                d.street,
                d.house,
                COUNT(DISTINCT e.employee_id) AS employee_count
            FROM department d
                LEFT JOIN employee e ON d.department_id = e.department_id
        """
        result = self._conn.execute(sql)
        return self._create_departments(result)

    def create_department(self, department: Department) -> None:
        sql = """
            INSERT INTO department 
                (city, street, house)
            VALUES
                (%S, %S, %S)
        """
        params = (department.city, department.street, department.house)
        self._conn.execute(sql, params)

    def update_department(self, department: Department) -> None:
        sql = """
            UPDATE department
            SET
                city = %s,
                street = %s,
                house = %s
            WHERE department_id = %s
        """
        params = (department.city, department.street, department.house, department.department_id)
        self._conn.execute(sql, params)

    def delete_department(self, department_id: int) -> None:
        sql = """
            DELETE FROM department
            WHERE department_id = %s
        """
        params = (department_id,)
        self._conn.execute(sql, params)

    @staticmethod
    def _create_departments(rows: List[Row]) -> List[Department]:
        models = []
        for row in rows:
            department = Department(
                department_id=row.department_id,
                city=row.city,
                street=row.street,
                house=row.house,
                employee_count=row.employee_count
            )
            models.append(department)
        return models
