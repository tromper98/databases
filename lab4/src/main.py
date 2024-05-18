import os
import sys


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    sys.path.append(parent_dir)
    from src.routes import app
    app.run(host='0.0.0.0', debug=True)
