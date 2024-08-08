import os
import sys
from flask_cors import CORS
from decouple import config as config_decouple
import logging
from logging.handlers import RotatingFileHandler
from init import init_app
from config_app import DevelopmentConfig, ProductionConfig

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

environment = config_decouple('FLASK_ENV', default='development')

if environment == 'development':
    config_class = DevelopmentConfig
else:
    config_class = ProductionConfig

app = init_app(config_class)
app.config['TIMEOUT'] = 300

CORS(app, resources={r"/*": {
    "origins": [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"]
}})

handler = RotatingFileHandler('flask.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
app.logger.addHandler(console_handler)
#health check
@app.route('/health', methods=['GET'])
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)