from flask import Flask, render_template, url_for, request, redirect


from src.app.model import *
from src.app.departmentservice import DepartmentService
from src.app.employeeservice import EmployeeService
from src.app.providers.departmentdbprovider import DepartmentDBProvider
from src.app.providers.employeedbprovider import EmployeeDBProvider

app = Flask(__name__)


@app.route('/department/all', methods=['GET', 'DELETE'])
def get_all_department():
    service = DepartmentService(DepartmentDBProvider())
    departments = service.get_departments()

    context = dict()
    context['departments'] = departments
    return render_template('department_all.html', **context)


@app.route('/department/department_id=<int:department_id>', methods=['GET', 'POST'])
def get_department_by_id(department_id: int):
    department_service = DepartmentService(DepartmentDBProvider())
    employee_service = EmployeeService(EmployeeDBProvider())

    department = department_service.get_department_by_id(department_id)
    employees = employee_service.get_employees_from_department(department.department_id)

    context = dict()
    context['department'] = department
    context['employees'] = employees
    return render_template('department.html', **context)


@app.route('/department/new', methods=['GET', 'POST'])
def new_department_page():
    return render_template('new_department.html')


@app.route('/department/create', methods=['POST'])
def create_department():
    if request.method == 'POST':
        service = DepartmentService(DepartmentDBProvider())
        dp = Department.from_dict(request.form)
        service.create_department(dp)
        return redirect('/department/all', code=302)


@app.route('/department/update', methods=['POST'])
def update_department():
    if request.method == 'POST':
        dp: Department = Department.from_dict(request.form)
        service = DepartmentService(DepartmentDBProvider())
        service.update_department(dp)
        return redirect(f'/department/department_id={dp.department_id}', code=302)


@app.route('/department/delete_employee/employee_id=<int:employee_id>', methods=['GET', 'POST', 'DELETE'])
def delete_employee_from_department(employee_id: int):
    service = EmployeeService(EmployeeDBProvider())
    employee = service.get_employee(employee_id)
    old_department_id = employee.department_id
    service.remove_employee_from_department(employee.employee_id)

    return redirect(f'/department/department_id={old_department_id}', code=302)


@app.route('/department/delete/department_id=<int:department_id>', methods=['GET', 'DELETE'])
def delete_department(department_id: int):
    department_service = DepartmentService(DepartmentDBProvider())
    employee_service = EmployeeService(EmployeeDBProvider())

    employees = employee_service.get_employees_from_department(department_id)
    for employee in employees:
        employee_service.remove_employee_from_department(employee.employee_id)

    department_service.delete_department(department_id)
    return redirect('/department/all', code=302)


@app.route('/employee/employee_id=<int:id>')
def get_employee_by_id(id):
    return render_template('employee.html')


@app.route('/')
def redirect_to_department_list():
    return get_all_department()
