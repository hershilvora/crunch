from app.api import api
from flask import session

@api.route('/create_session')
def create_session(current_user):
    session['current_user'] = current_user
