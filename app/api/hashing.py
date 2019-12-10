from app.api import api
import hashlib
import json

def hash_password(password):
    data = json.loads(password)
    password = data["password"]

    salt = '5gg885kfd9903'
    db_password = password + salt
    passwordhash = (hashlib.md5(db_password.encode())).hexdigest()

    info = {
        "passwordhash": passwordhash
    }

    return json.dumps(info)
