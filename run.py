import logging
import os
from flask import Flask
from flask_cors import CORS
from app.routes.books import books_bp
from app.routes.ping import ping_bp
import requests
from config import Config

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object(Config)
app.secret_key = '1234'


app.register_blueprint(books_bp)
app.register_blueprint(ping_bp)


def check_flask_is_running():
    ping_test_ip = 'http://localhost:5004/ping'
    try:
        response = requests.get(ping_test_ip, timeout=10)
        if response.status_code == 200:
            logging.info('Flask is already running on port 5002')
            return True
    except requests.RequestException as e:
        logging.warning(f'An exception occurred while checking '
                        f'Flask status: {e}')
    return False


def initialize_logging():
    pid = os.getpid()
    logging.info(f'Processor ID (PID): {pid}')
    with open('pid.txt', 'w') as f:
        f.write(f'{pid}')


if __name__ == '__main__':
    if not check_flask_is_running():
        initialize_logging()

        run_config = {
            'host': Config.APP_IP,
            'port': Config.PORT,
            'debug': Config.DEBUG,
            'threaded': True,
            'use_reloader': False,
            'passthrough_errors': True,
            'use_debugger': False
        }

        app.run(**run_config)
