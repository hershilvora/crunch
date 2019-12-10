from app.api import api
from app import Database
import mysql.connector
import json

@api.route('/create_ticket', methods=["GET"])
def create_ticket(info):
    data = json.loads(info)
    user = data["user"]
    ticket_id = data["ticket_id"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "INSERT INTO tickets (ticket_id, user, status) VALUES  (%s, %s, %s)"
    values = (ticket_id, user, 'Unresolved')
    result = Database.execStatement(myDb, sqlString, values)
    myDb.commit()

@api.route('/update_ticket', methods=["GET"])
def update_ticket(info):
    data = json.loads(info)
    ticket_id = data["ticketID"]

    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "UPDATE tickets SET status = 'Resolved' WHERE ticket_id = %s"
    value = ticket_id
    result = Database.execStatement(myDb, sqlString), value
    myDb.commit()

@api.route('/get_tickets', methods=["GET"])
def get_tickets():
    myDb = Database.dbConnection()
    print(myDb)
    sqlString = "SELECT * FROM tickets"
    result = Database.selectStatement(myDb, sqlString)
    fetch = result.fetchall()
    info = {}
    for ticket in fetch:
        info[ticket[0]] = {
            "ticket_id": ticket[0],
            "user": ticket[1],
            "status": ticket[2]
        }
    return json.dumps(info)