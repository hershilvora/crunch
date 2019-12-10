from app.api import api
from app import Database
import mysql.connector
import json


@api.route('/create_user', methods=['POST'])
def create_user(user_info):
    data = json.loads(user_info)
    email = data["email"]
    userName = data["userName"]
    passwordHash = data["passwordHash"]
    fullName = data["fullName"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "INSERT INTO users (email, userName, passwordHash, fullName) VALUES (%s, %s, %s, %s)"
    values = (email, userName, passwordHash, fullName)
    result = Database.execStatement(myDb, sqlString, values)
    myDb.commit()
    #return(result)



@api.route('/check_user',methods=['GET'])
def check_user(user_info):
    data = json.loads(user_info)
    email = data["email"]
    userName = data["userName"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString_Email = "SELECT email FROM users WHERE email = %s"
    value_email = email
    sqlString_UserName = "SELECT userName FROM users WHERE userName = %s"
    value_username = userName
    result1 = Database.execStatement(myDb, sqlString_Email, value_email)
    result2 = Database.execStatement(myDb, sqlString_UserName, value_username)
    if (result1.rowcount != 0):
        return 'email taken'
    elif (result2.rowcount != 0):
        return 'username taken'
    else:
        return 'clear'




@api.route('/get_user', methods=['GET'])
def get_user(login_info):
    data = json.loads(login_info)
    email = data["email"]
    passwordHash = data["passwordhash"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT passwordHash, userid FROM users WHERE email = %s"
    value_email = email
    result = Database.execStatement(myDb, sqlString)
    if(result.rowcount == 1):
        fetch = result.fetchone()
        if (fetch[0] == passwordHash):
            return fetch[1]
    else:
        return False

@api.route('/get_subscribers', methods=["GET"])
def get_subscribers():
    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT email FROM users WHERE isSubscribed = '1'"
    result = Database.execStatement(myDb, sqlString)
    fetch = result.fetchall()
    emailList = []
    for i in fetch:
        emailList.append(i[0])
    return emailList

@api.route('/update_name', methods=["GET"])
def update_name(update_info):
    data = json.loads(update_info)
    name = data["name"]
    userid = str(data["userid"])
    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "UPDATE users SET fullname = %s WHERE userid = %s "
    values = (name, userid)
    result = Database.execStatement(myDb, sqlString, values)
    myDb.commit()

@api.route('/update_subscription', methods=["GET"])
def update_subscription(update_info):
    data = json.loads(update_info)
    status = str(data["status"])
    userid = str(data["userid"])
    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "UPDATE users SET isSubscribed = %s WHERE userid = %s"
    values = (status, userid)
    result = Database.execStatement(myDb, sqlString, values)
    myDb.commit()

@api.route('/get_user_info', methods=["GET"])
def get_user_info(info):
    data = json.loads(info)
    userid = str(data["userid"])
    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT username, fullname, isSubscribed FROM users WHERE userid = %s"
    value = userid
    result = Database.execStatement(myDb, sqlString, value)
    fetch = result.fetchall()
    if fetch != None:
        user_info = {
            "status": 1,
            "username": fetch[0][0],
            "fullname": fetch[0][1],
            "isSubscribed": fetch[0][2]
        }
    else:
        user_info = {
            "status": 0
        }
    return json.dumps(user_info)

@api.route('/change_password', methods=["GET"])
def change_password(info):
    data = json.loads(info)
    current_hash = data["current_hash"]
    change_hash = data["change_hash"]
    userid = str(data["userid"])
    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "UPDATE users SET passwordHash = %s WHERE userid = %s AND passwordHash = %s"
    values = (current_hash, userid, change_hash)
    result = Database.execStatement(myDb, sqlString, values)
    myDb.commit()




