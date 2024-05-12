from flask import Flask, render_template

from src.app.departmentservice import DepartmentService
from src.app.providers.departmentdbprovider import DepartmentDBProvider

app = Flask(__name__)


@app.route('/department/all')
def get_all_department():
    return render_template('department_all.html')


@app.route('/department/department_id=<int:department_id>')
def get_department_by_id(department_id: int):
    service = DepartmentService(DepartmentDBProvider())
    department = service.get_department_by_id(department_id)
    context = department.to_dict()
    return render_template('department.html', **context)


@app.route('/employee/employee_id=<int:id>')
def get_employee_by_id(id):
    return render_template('employee.html')


@app.route('/')
def redirect_to_department():
    return get_all_department()
