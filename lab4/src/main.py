import os
import sys

# Именовать как константы
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

if __name__ == '__main__':
    sys.path.append(parent_dir)
    from src.routes import app
    app.run(host='0.0.0.0', debug=True)
