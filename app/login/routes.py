import json
from flask import render_template, redirect, request, flash, session, url_for
from app.login import login_bp
from app.api import users, hashing
# from flask_login import current_user, login_user

@login_bp.route('/login_page',methods=['GET','POST'])
def login_page():
    error = None
    error1 = "Email"
    error2 = "Password"

    if request.method == "POST":
        email = request.form.get('email', False)

        password = request.form.get('password', False)
        to_hash = {
            "password": password
        }
        hash = hashing.hash_password(json.dumps(to_hash))
        info = json.loads(hash)
        pH = info["passwordhash"]

        info = {
            "email": email,
            "passwordhash": pH
        }

        json_info = json.dumps(info)
        user = users.get_user(json_info)
        if (user == False):
            error1 = "Login information is incorrect!"
            error2 = "Login information is incorrect!"
            info = {
                "status": "Failure"
            }
        else:
            error = None
            session['userid'] = user
            return redirect(url_for('index'))

    return render_template("login.html", error=error, error1=error1, error2=error2)

@login_bp.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('userid', None)
    return redirect(url_for('index'))


