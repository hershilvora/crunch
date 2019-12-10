import json
from flask import render_template, request, flash, redirect, url_for
from app.signup import signup_bp
from app.api import users,hashing
import hashlib



@signup_bp.route('/signup_page', methods=['POST', 'GET'])
def signup_page():

    error = None
    error1 = "Email"
    error2 = "Username"

    if request.method == 'POST':
        fullname = request.form.get('fullName', False)
        email = request.form.get('email', False)
        username = request.form.get('username', False)

        password = request.form.get('password', False)
        to_hash = {
                "password" : password
        }
        hash = hashing.hash_password(json.dumps(to_hash))
        info = json.loads(hash)
        passwordhash = info["passwordhash"]

        info = {
            "email": email,
            "userName": username,
            "passwordHash": passwordhash,
            "fullName": fullname
        }
        json_info = json.dumps(info)
        check = users.check_user(json_info)


        if(check == 'clear'):
            users.create_user(json_info)
            error = None
            return redirect(url_for('login.login_page'))
        elif(check == 'email taken'):
            error1 = "The email is already taken!"
            info = {
                "status": "email taken"
            }
        elif(check == 'username taken'):
            error2 = "The username is already taken!"
            info = {
                "status": "username taken"
            }
        #return json.dumps(info)

    return render_template('signup.html', error=error, error1=error1, error2=error2)

