from flask import Blueprint

recommend_bp = Blueprint('recommend', __name__, url_prefix='/recommend')

from app.recommend import routes