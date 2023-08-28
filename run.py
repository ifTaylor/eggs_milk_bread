import logging
import os
from app import create_app
from flask import request
import requests
from config import Config

logging.basicConfig(level=logging.INFO)


def check_flask_is_running():
    ping_test_ip = 'http://localhost:5004/ping'
    try:
        response = request.get(ping_test_ip, timeout=10)
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
        app = create_app()
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
