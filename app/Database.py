import mysql.connector

def dbConnection():
    dbHost = '************'
    dbUser = '*********'
    dbPassword = '**********'
    db = '9uAko4qR3y'

    mydb = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPassword, database=db)
    if(mydb):
        return mydb
    else:
        return None

def selectStatement(dbConnection, sqlQuery):
    dbCursor = dbConnection.cursor(buffered=True)
    dbCursor.execute(sqlQuery)
    return dbCursor

def execStatement(dbConnection, sqlQuery, values):
    dbCursor = dbConnection.cursor()
    dbCursor.execute(sqlQuery, values)
    return dbCursor