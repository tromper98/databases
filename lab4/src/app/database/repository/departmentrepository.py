import os
from typing import List

from pyodbc import Row

from src.app.database.model.department import Department
from src.app.common.dbconnection import DbConnection


class DepartmentRepository:

    def __init__(self) -> None:
        self._conn = DbConnection(os.environ.get('POSTGRES_CONN_STR'))

    def find(self, department_id: int) -> Department:
        sql = """
            SELECT
                department_id,
                city,
                street,
                house
            FROM department
            WHERE department_id = ?
        """
        params = (department_id,)
        result = self._conn.select(sql, params)
        return self._create_department(result[0])

    def find_all(self) -> List[Department]:
        sql = """
            SELECT
                department_id,
                city,
                street,
                house
            FROM department
        """
        result = self._conn.select(sql)
        return [self._create_department(row) for row in result]

    def get_employee_count(self, department_id: int) -> int:
        sql = """
            SELECT 
                COUNT(*) AS employee_count
            FROM employee
            WHERE department_id = ?
            GROUP BY department_id
        """
        params = (department_id,)
        result = self._conn.select(sql, params)
        if len(result) == 0:
            return 0
        return result[0].employee_count

    def store(self, department: Department) -> None:
        if department.department_id:
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
        else:
            sql = """
                INSERT INTO department 
                    (city, street, house)
                VALUES
                    (?, ?, ?)
            """
            params = (department.city, department.street, department.house)
            self._conn.insert(sql, params)

    def remove(self, department_id: int) -> None:
        self._remove_employee_from_department(department_id)
        sql = """
            DELETE FROM department
            WHERE department_id = ?
        """
        params = (department_id,)
        self._conn.delete(sql, params)

    def _remove_employee_from_department(self, department_id: int) -> None:
        sql = """
            DELETE FROM employee
            WHERE department_id = ?
        """
        params = (department_id,)
        self._conn.delete(sql, params)

    @staticmethod
    def _create_department(row: Row) -> Department:
        return Department(
            department_id=row.department_id,
            city=row.city,
            street=row.street,
            house=row.house,
        )
