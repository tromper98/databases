from flask import Flask

app = Flask(__name__)


@app.route('/department/all')
def get_all_department():
    return """
    <h1> All Department </h1>"""


@app.route('/department/department_id=<id>')
def get_department_by_id(id):
    return f"""
    <h1> Department {id}"""


if __name__ == '__main__':
    app.run(host='0.0.0.0')
