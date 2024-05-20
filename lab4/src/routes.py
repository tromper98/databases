from flask import Flask, render_template, request, redirect


from src.app.model import *
from src.app import DepartmentService, EmployeeService, JobTitleService
from src.app.providers.departmentdbprovider import DepartmentDBProvider
from src.app.providers.employeedbprovider import EmployeeDBProvider
from src.app.providers.jobtitledbprovider import JobTitleDBProvider

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
    context['navbar_department'] = department
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


@app.route('/department/delete/department_id=<int:department_id>', methods=['GET', 'DELETE'])
def delete_department(department_id: int):
    department_service = DepartmentService(DepartmentDBProvider())
    employee_service = EmployeeService(EmployeeDBProvider())

    employees = employee_service.get_employees_from_department(department_id)
    for employee in employees:
        employee_service.delete_employee(employee.employee_id)

    department_service.delete_department(department_id)
    return redirect('/department/all', code=302)


@app.route('/employee/employee_id=<int:employee_id>')
def get_employee_by_id(employee_id: int):
    employee_service = EmployeeService(EmployeeDBProvider())
    job_title_service = JobTitleService(JobTitleDBProvider())
    department_service = DepartmentService(DepartmentDBProvider())

    context = dict()
    employee = employee_service.get_employee(employee_id)

    context['navbar_employee'] = employee
    context['navbar_department'] = department_service.get_department_by_id(employee.department_id)
    context['employee'] = employee
    context['departments'] = department_service.get_departments()
    context['job_titles'] = job_title_service.get_job_titles()
    return render_template('employee.html', **context)


@app.route('/employee/new', methods=['GET', 'POST'])
def new_employee():
    context = dict()
    department_service = DepartmentService(DepartmentDBProvider())
    job_title_service = JobTitleService(JobTitleDBProvider())
    if request.method == 'POST' and 'department_id' in request.form.keys():
        dp = department_service.get_department_by_id(int(request.form['department_id']))

        context['navbar_department'] = dp
        context['source_department'] = dp

    context['departments'] = department_service.get_departments()
    context['job_titles'] = job_title_service.get_job_titles()

    return render_template('new_employee.html', **context)


@app.route('/employee/create', methods=['POST'])
def create_employee():
    if request.method == 'POST':
        service = EmployeeService(EmployeeDBProvider())
        emp = Employee.from_dict(request.form)
        service.create_employee(emp)
        return redirect(f'/department/department_id={emp.department_id}', code=302)


@app.route('/employee/update', methods=['POST'])
def update_employee():
    if request.method == 'POST':
        emp: Employee = Employee.from_dict(request.form)
        service = EmployeeService(EmployeeDBProvider())
        service.update_employee(emp)
        return redirect(f'/employee/employee_id={emp.employee_id}', code=302)


@app.route('/employee/delete/employee_id=<int:employee_id>', methods=['GET', 'DELETE'])
def delete_employee(employee_id: int):
    service = EmployeeService(EmployeeDBProvider())
    emp = service.get_employee(employee_id)
    service.delete_employee(emp.employee_id)
    return redirect(f'/department/department_id={emp.department_id}', code=302)


@app.route('/')
def redirect_to_department_list():
    return redirect(f'/department/all', code=302)
