from flask import Flask, render_template


app = Flask(__name__)


@app.route('/department/all')
def get_all_department():
    return render_template('department_all.html')


@app.route('/department/department_id=<int:id>')
def get_department_by_id(id):
    return render_template('department.html')


@app.route('/employee/employee_id=<int:id>')
def get_employee_by_id(id):
    return render_template('employee.html')


@app.route('/')
def redirect_to_department():
    return get_all_department()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
