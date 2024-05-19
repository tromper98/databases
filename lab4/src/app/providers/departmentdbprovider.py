from typing import List
import os

from pyodbc import Row
from src.app.departmentservice import DepartmentProvider
from src.app.model.department import Department
from src.app.common.dbconnection import DbConnection


class DepartmentDBProvider(DepartmentProvider):

    def __init__(self):
        self._conn = DbConnection(os.environ.get('POSTGRES_CONN_STR'))

    def is_department_exists(self, department_id: int) -> bool:
        sql = f"""
            SELECT 
                1
            FROM department
            WHERE department_id = ?
        """

        params = (department_id,)
        result = self._conn.select(sql, params)
        if result is not None:
            return True
        return False

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
        result = self._conn.select(sql, params)
        return Department.from_query_result(result[0])

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
            GROUP BY
                d.department_id,
                d.city,
                d.street,
                d.house
        """
        result = self._conn.select(sql)
        return [Department.from_query_result(row) for row in result]

    def create_department(self, department: Department) -> None:
        sql = """
            INSERT INTO department 
                (city, street, house)
            VALUES
                (?, ?, ?)
        """
        params = (department.city, department.street, department.house)
        self._conn.insert(sql, params)

    def update_department(self, department: Department) -> None:
        sql = """
            UPDATE department
            SET
                city = ?,
                street = ?,
                house = ?
            WHERE department_id = ?
        """
        params = (department.city, department.street, department.house, department.department_id)
        self._conn.update(sql, params)

    def delete_department(self, department_id: int) -> None:
        sql = """
            DELETE FROM department
            WHERE department_id = ?
        """
        params = (department_id,)
        self._conn.delete(sql, params)
