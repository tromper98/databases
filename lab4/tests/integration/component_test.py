import pytest
import os
import sys


from datetime import date

# Именовать как константы
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
APP_DIR = os.path.join(PROJECT_DIR, 'src')
sys.path.append(APP_DIR)


from src.app.common.dbconnection import DbConnection
from src.app.common.transfer.departmentdto import DepartmentDTO
from src.app.common.transfer.employeedto import EmployeeDTO
from src.app.database.repository import *
from src.app.database.model import *


@pytest.fixture
def truncate_tables_after_test():
    yield
    conn = DbConnection(os.environ.get('POSTGRES_CONN_STR'))
    conn.execute('TRUNCATE TABLE employee RESTART IDENTITY CASCADE')
    conn.execute('TRUNCATE TABLE department RESTART IDENTITY CASCADE')


def assert_department(first: Department, second: Department) -> bool:
    if first.city != second.city:
        return False

    if first.street != second.street:
        return False

    if first.house != second.house:
        return False

    return True


def assert_employee(first: Employee, second: Employee) -> bool:
    if first.first_name != second.first_name:
        return False

    if first.last_name != second.last_name:
        return False

    if first.middle_name != second.middle_name:
        return False

    if first.birth_date != second.birth_date:
        return False

    if first.sex != second.sex:
        return False

    if first.job_title_id != second.job_title_id:
        return False

    if first.hire_date != second.hire_date:
        return False

    if first.email != second.email:
        return False

    if first.phone != second.phone:
        return False

    if first.note != second.note:
        return False

    return True


@pytest.mark.usefixtures('truncate_tables_after_test')
def test_department_operations():
    department_repository = DepartmentRepository()
    employee_repository = EmployeeRepository()

    # Test create department
    dep = Department('city_1', 'street_1', 'house_1')

    department_repository.store(dep)
    stored_dep = department_repository.find(1)

    assert assert_department(dep, stored_dep)

    # Test update department
    dep_dto = DepartmentDTO(dep.city, dep.street, 'house_2')
    stored_dep.edit(dep_dto)

    department_repository.store(stored_dep)
    stored_dep = department_repository.find(1)

    expected = Department('city_1', 'street_1', 'house_2')
    assert assert_department(expected, stored_dep)

    # Test calculate department employee number
    emp_1 = Employee(first_name='f_name_1',
                     last_name='l_name_1',
                     email='test@example.com',
                     phone='89001112233',
                     birth_date=date(1990, 1, 1),
                     hire_date=date(2020, 1, 1),
                     job_title_id=1,
                     department_id=1)
    employee_repository.store(emp_1)

    assert department_repository.get_employee_count(1) == 1

    emp_2 = Employee(first_name='f_name_2',
                     last_name='l_name_2',
                     email='test2@example.com',
                     phone='89011112233',
                     birth_date=date(1990, 1, 2),
                     hire_date=date(2020, 1, 2),
                     job_title_id=2,
                     department_id=1)
    employee_repository.store(emp_2)

    assert department_repository.get_employee_count(1) == 2

    emp_3 = Employee(first_name='f_name_3',
                     last_name='l_name_3',
                     email='test3@example.com',
                     phone='89021112233',
                     birth_date=date(1990, 1, 3),
                     hire_date=date(2020, 1, 3),
                     job_title_id=3,
                     department_id=1)
    employee_repository.store(emp_3)

    assert department_repository.get_employee_count(1) == 3

    # Test get department employees
    expected_employees = [emp_1, emp_2, emp_3]
    employees = employee_repository.find_by_department_id(1)
    assert all(assert_employee(x, y) for x, y in zip(employees, expected_employees))

    # Test delete department

    department_repository.remove(1)

    assert department_repository.find(1) is None


@pytest.mark.usefixtures('truncate_tables_after_test')
def test_employee_operations():

    # Test create employee
    employee_repository = EmployeeRepository()
    emp = Employee(first_name='f_name',
                   last_name='l_name',
                   middle_name='m_name',
                   sex='M',
                   email='test@example.com',
                   phone='89001112233',
                   birth_date=date(1990, 1, 1),
                   hire_date=date(2020, 1, 1),
                   note='aaaaaa',
                   job_title_id=1)
    employee_repository.store(emp)
    stored_emp = employee_repository.find(1)

    assert assert_employee(emp, stored_emp)

    # Test update employee

    emp_dto = EmployeeDTO(
        employee_id=1,
        first_name='f_name_new',
        last_name='l_name_new',
        middle_name='m_name_new',
        sex='M',
        email='test@example.com',
        phone='89001112233',
        birth_date=date(1990, 1, 1),
        hire_date=date(2024, 1, 1),
        note='aaaaaa',
        job_title_id=2,
        department_id=None,
        image_path=None)

    expected_emp = Employee.from_dto(emp_dto)
    stored_emp.edit(emp_dto)
    employee_repository.store(stored_emp)
    stored_emp = employee_repository.find(1)

    assert assert_employee(stored_emp, expected_emp)

    # Test delete employee

    employee_repository.remove_by_ids([stored_emp.employee_id])

    assert employee_repository.find(1) is None
