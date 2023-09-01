from flask import Blueprint, session

ping_bp = Blueprint('ping', __name__)


@ping_bp.route('/ping')
def ping():
    user_id = session.get('user_id')
    return f'Hi, I am alive! Pinger: {user_id}'
