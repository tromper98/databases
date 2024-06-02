from flask import Flask, render_template, request, redirect, send_from_directory

from src.app.common.filehandler import FileHandler
from src.app.common.transfer.employeedto import EmployeeDTO
from src.app.common.transfer.departmentdto import DepartmentDTO

from src.app.database.repository import EmployeeRepository, DepartmentRepository
from src.app.database.model import Employee, Department
from src.app.database.providers.jobtitledbprovider import JobTitleDBProvider

app = Flask(__name__)


# TODO проверить HTTP методы

@app.route('/department/all')
def get_all_department():
    repository = DepartmentRepository()
    departments = repository.find_all()

    dto_list = []
    if departments:
        for department in departments:
            dto_list.append(DepartmentDTO(
                department_id=department.department_id,
                city=department.city,
                street=department.street,
                house=department.house,
                employee_count=repository.get_employee_count(department.department_id)
            ))

    context = dict(
        departments=dto_list
    )
    return render_template('department_all.html', **context)


@app.route('/department/department_id=<int:department_id>', )
def get_department_by_id(department_id: int):
    department_repository = DepartmentRepository()
    employee_repository = EmployeeRepository()

    department = department_repository.find(department_id)
    if not department:
        raise ValueError(f'Department with department_id={department_id} not found')
    employees = employee_repository.find_by_department_id(department.department_id)

    context = dict(
        navbar_department=department,
        department=department,
        employees=employees
    )
    return render_template('department.html', **context)


@app.route('/department/new')
def new_department():
    return render_template('new_department.html')


@app.route('/department/create', methods=['POST'])
def create_department():
    dto = DepartmentDTO.from_dict(request.form)
    department = Department(dto.city, dto.street, dto.house)

    repository = DepartmentRepository()
    repository.store(department)
    return redirect('/department/all', code=302)


@app.route('/department/update', methods=['POST'])
def update_department():
    dto = DepartmentDTO.from_dict(request.form)
    repository = DepartmentRepository()
    department = repository.find(dto.department_id)
    if not department:
        raise ValueError(f'Department with department_id={dto.department_id} not found')
    department.edit(dto)
    repository.store(department)
    return redirect(f'/department/department_id={department.department_id}', code=302)


@app.route('/department/delete/department_id=<int:department_id>', methods=['GET'])
def delete_department(department_id: int):
    repository = DepartmentRepository()
    repository.remove(department_id)
    return redirect('/department/all', code=302)


@app.route('/employee/employee_id=<int:employee_id>')
def get_employee_by_id(employee_id: int):
    employee_repository = EmployeeRepository()
    department_repository = DepartmentRepository()
    job_title_provider = JobTitleDBProvider()

    employee = employee_repository.find(employee_id)
    if not employee:
        raise ValueError(f'Employee with employee_id={employee_id} not found')

    context = dict(
        navbar_employee=employee,
        navbar_department=department_repository.find(employee.department_id),
        employee=employee,
        departments=department_repository.find_all(),
        job_titles=job_title_provider.find_all()
    )
    return render_template('employee.html', **context)


@app.route('/employee/new')
def new_employee():
    department_repository = DepartmentRepository()
    job_title_provider = JobTitleDBProvider()

    dp = department_repository.find(int(request.form['department_id']))
    context = dict(
        navbar_department=dp,
        source_department=dp,
        departments=department_repository.find_all(),
        job_titles=job_title_provider.find_all()
    )
    return render_template('new_employee.html', **context)


@app.route('/employee/create', methods=['POST'])
def create_employee():
    dto = EmployeeDTO.from_dict(request.form)
    if 'photo' in request.files:
        file = request.files['photo']
        file_handler = FileHandler(app.config['UPLOAD_FOLDER'])
        if file_handler.try_save_file(file):
            dto.image_path = file.filename

    employee = Employee.from_dto(dto)
    repository = EmployeeRepository()

    repository.store(employee)
    return redirect(f'/department/department_id={employee.department_id}', code=302)


@app.route('/employee/update', methods=['POST'])
def update_employee():
    repository = EmployeeRepository()

    dto = EmployeeDTO.from_dict(request.form)
    if 'photo' in request.files:
        file = request.files['photo']
        file_handler = FileHandler(app.config['UPLOAD_FOLDER'])
        if file_handler.try_save_file(file):
            dto.image_path = file.filename

    employee = repository.find(dto.employee_id)
    if not employee:
        raise ValueError(f'Employee with employee_id={dto.employee_id} not found')
    employee.edit(dto)

    repository.store(employee)
    return redirect(f'/employee/employee_id={employee.employee_id}', code=302)


@app.route('/employee/delete/employee_id=<int:employee_id>')
def delete_employee(employee_id: int):
    repository = EmployeeRepository()
    employee = repository.find(employee_id)
    repository.remove_by_ids([employee_id])
    return redirect(f'/department/department_id={employee.department_id}', code=302)


@app.route('/')
def redirect_to_department_list():
    return redirect(f'/department/all', code=302)


@app.route('/public/uploads/<path:filename>')
def upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
