#So create a "Database.py" within the app folder.  This will have the functions you need to access the database on your
#own machine.  Make sure you already have the database set up.

import mysql.connector #youll need to install the mysql-connector-python package.  If you have pycharm, go into
                        #file>settings>project: "*name of project*">project interpreter> click the plus, search for
                        #mysql-connector-python and install that one.  Just the normal one, not the dd or rf one.

def dbConnection():
    dbHost = 'localhost'
    dbUser = '' #type in the user you set up when installing mysql.
    dbPassword = '' #type the password you set up when installing mysql.
    db = 'moviedb' #This should be the name of your db schema.

    #This creates a connection to the database and returns the connection.  Make sure that your database is running.
    mydb = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPassword, database=db)
    if(mydb):
        return mydb
    else:
        return None

#These two are basically the exact same fucntions. The difference is the execStatement fucntion takes in a values
#argument for times when you are trying to search or insert several values.  You can see examples of a sqlQuery in the
#api.users or movie_search files.
def selectStatement(dbConnection, sqlQuery):
    dbCursor = dbConnection.cursor(buffered=True)
    dbCursor.execute(sqlQuery)
    return dbCursor

def execStatement(dbConnection, sqlQuery, values):
    dbCursor = dbConnection.cursor()
    dbCursor.execute(sqlQuery, values)
    return dbCursor

