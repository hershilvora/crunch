from flask import Blueprint

signup_bp = Blueprint('signup', __name__, url_prefix='/signup')

from app.signup import routes