from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from app.api import users, hashing, session, movie_search, web_scraper