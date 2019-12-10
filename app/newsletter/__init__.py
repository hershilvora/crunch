from flask import Blueprint

newsletter_bp = Blueprint('newsletter', __name__, url_prefix='/newsletter')

from app.newsletter import routes