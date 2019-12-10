from flask import Flask, render_template, session
import json
from app.api import users

app = Flask(__name__)
app.config['SECRET_KEY'] = "my_secret_string"

@app.route("/", methods=["GET", "POST"])
def index():
    username = None
    if "userid" in session:
        userid = session["userid"]
        info = {
            "userid": userid
        }
        data = json.loads(users.get_user_info(json.dumps(info)))
        username = data["username"]
    return render_template('index.html', username=username)

from app.api import api as api_bp
app.register_blueprint(api_bp)

from app.login import login_bp as login_bp
app.register_blueprint(login_bp)

from app.search import search_bp as search_bp
app.register_blueprint(search_bp)

from app.signup import signup_bp as signup_bp
app.register_blueprint(signup_bp)

from app.newsletter import newsletter_bp as newsletter_bp
app.register_blueprint(newsletter_bp)

from app.profile import profile_bp as profile_bp
app.register_blueprint(profile_bp)

from app.recommend import recommend_bp as recommend_bp
app.register_blueprint(recommend_bp)

from app.support import support_bp as support_bp
app.register_blueprint(support_bp)

from app.recommend import recommend_bp as recommend_bp
app.register_blueprint(recommend_bp)