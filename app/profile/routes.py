from app.profile import profile_bp
from app.api import users, hashing
from flask import render_template, session, redirect, url_for, request
import json

@profile_bp.route('/profile_page', methods=["GET","POST"])
def profile_page():
    if "userid" in session:
        userid = session["userid"]
        info = {
            "userid": userid
        }
        data = json.loads(users.get_user_info(json.dumps(info)))
        username = data["username"]
        fullname = data["fullname"]
        isSubscribed = data["isSubscribed"]

        if request.method == "POST":
            if request.form['submit'] == 'change_name':
                fullname = request.form.get("fullname", False)
                name_change_info = {}
                if fullname != False:
                    name_change_info = {
                        "name": fullname,
                        "userid": userid
                    }
                users.update_name(json.dumps(name_change_info))
            elif request.form['submit'] == "change_password":
                current_pass = request.form.get("current_password", False)
                change_pass = request.form.get("password_change", False)
                if current_pass != False and change_pass != False:
                    info = {
                        "password": current_pass
                    }
                    current_hash = json.loads(hashing.hash_password(json.dumps(info)))
                    info = {
                        "password": change_pass
                    }
                    change_hash = json.loads(hashing.hash_password(json.dumps(info)))
                    password_change = {
                        "userid": userid,
                        "current_hash": current_hash["passwordhash"],
                        "change_hash": change_hash["passwordhash"]
                    }
                    users.change_password(json.dumps(password_change))
            elif request.form['submit'] == 'Unsubscribe':
                subscription_info = {
                    "status": 0,
                    "userid": userid
                }
                users.update_subscription(json.dumps(subscription_info))
                isSubscribed = 0
                return render_template('profile_page.html', username=username, fullname=fullname, isSubscribed=isSubscribed)
            elif request.form['submit'] == 'Subscribe':
                subscription_info = {
                    "status": 1,
                    "userid": userid
                }
                isSubscribed = 1
                users.update_subscription(json.dumps(subscription_info))
                return render_template('profile_page.html', username=username, fullname=fullname,
                                   isSubscribed=isSubscribed)
        return render_template('profile_page.html', username=username, fullname=fullname, isSubscribed=isSubscribed, userid=userid)
    return redirect(url_for('login.login_page'))
