import os
import sys

# Именовать как константы
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)

UPLOAD_FOLDER = os.path.join(SCRIPT_DIR, 'public', 'uploads')

if __name__ == '__main__':
    sys.path.append(PARENT_DIR)
    from src.routes import app
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(host='0.0.0.0', debug=True)
