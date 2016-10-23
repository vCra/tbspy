"""
SQL Stuff
This is where all of the SQL commands that are used are kept. All SQL Commands should be done via this file
"""
import sqlite3
import os
import sys
import settings
database= settings.SQLiteDBLocation
def init(db=database,again="nope"):
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        return db,connection,cursor
        print("1")
    except:
        connection.close()
        open(db, 'w+')
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        print("2")
        return db,connection,cursor
        
db,connection,cursor = init()
def createTables():
    db,connection,cursor = init()
    deleteDatabase()
    db,connection,cursor = init()
    venue.table()
    event.table()
    customer.table()
    ticket.table()

def close(connection=connection):
    connection.commit()
    connection.close()
    sys.exit

def deleteDatabase():
    close()
    os.remove(database)
    db,connection,cursor = init()
    

###############################################################

class ticket():
    """
    Handles the creation, edition and deletion of ticket objects.
    """
    def table():
        ticketTableSQL ="""
                CREATE TABLE "ticket" (
                    "id" integer NOT NULL PRIMARY KEY,
                    "owner_id" integer NOT NULL REFERENCES "customer" ("id"),
                    "event_id" integer NOT NULL REFERENCES "event" ("id"),
                    "booking_id" integer NOT NULL
                );
            """
        cursor.execute(ticketTableSQL)
    def last():
        cursor.execute("SELECT MAX(id) AS id FROM ticket")
        lastID = cursor.fetchall()
        return lastID[0][0]
    def create(owner,event):
        cursor.execute("INSERT INTO ticket VALUES (null, '%s', '%s')" % (owner, event))
        connection.commit()
    def all():
        cursor.execute("SELECT id, owner_id, event_id FROM ticket ORDER BY id")
        venuelist = cursor.fetchall()
        return venuelist
    def get(id):
        query = "SELECT * from ticket WHERE id = " + str(id)
        cursor.execute(query)
        ticket = cursor.fetchall()
        return ticket

##########################################################################

class customer():
    def getLastCustomerID():
        cursor.execute("SELECT MAX(id) AS id FROM customer")
        lastID = cursor.fetchall()
        return lastID[0][0]
    def get(id):
        query = "SELECT * from customer WHERE id = " + str(id)
        cursor.execute(query)
        customer = cursor.fetchall()
        return customer
    def table():
        customerTableSQL ="""
            CREATE TABLE "customers" (
                "id" integer NOT NULL PRIMARY KEY,
                "first_name" varchar(100) NOT NULL,
                "last_name" varchar(100) NOT NULL,
                "address" varchar(255) NOT NULL,
                "town" varchar(50) NOT NULL,
                "postcode" varchar(10),
                "phone_number" integer
            );
        """
        cursor.execute(customerTableSQL)

#############################################################################

class event():
    """
    SQL Handles for Objects in the Events Table
    """
    def allstdout():
        cursor.execute("SELECT * FROM event ORDER BY name")
        eventList = cursor.fetchall()
        for thing in eventList:
            print("Event Name: ",thing[1])
            print("Event Details: ",thing[2])
    def all():
        cursor.execute("SELECT id, name, date FROM event ORDER BY name")
        venuelist = cursor.fetchall()
        return venuelist
    def create(name,details,date,time,venue_id,website,featured):
        cursor.execute("INSERT INTO event VALUES (null, '%s','%s','%s','%s','%s','%s','%s')" % (name,details,date,time,venue_id,website,featured))
        connection.commit()
    def last():
        cursor.execute("SELECT MAX(id) AS id FROM event")
        lastID = cursor.fetchall()
        return lastID[0][0]
    def get(id):
        query = "SELECT * from event WHERE id = " + str(id)
        cursor.execute(query)
        event = cursor.fetchall()
        return event
    def table():
        eventTableSQL = """
            CREATE TABLE "event" (
                "id" integer NOT NULL PRIMARY KEY,
                "name" varchar(100) NOT NULL,
                "details" text,
                "date" date NOT NULL,
                "time" time NOT NULL,
                "venue_id" integer NOT NULL REFERENCES "venue" ("id"),
                "website" varchar(200),
                "featured" bool NOT NULL
            );
            """
        cursor.execute(eventTableSQL)


########################################################################

class venue():
    """
    SQL Handles for Objects in the venue Table
    """
    def all(orderby = "name"):
        query = "SELECT id, name FROM venue ORDER BY " + orderby
        cursor.execute(query)
        venuelist = cursor.fetchall()
        return venuelist
    def getLastVenueID():
        cursor.execute("SELECT MAX(id) AS id FROM veune")
        lastID = cursor.fetchall()
        return lastID[0][0]
    def create(name,details,address,town,postcode,website,phone,featured):
        cursor.execute("INSERT INTO venue VALUES (null, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (name,details,address,town,postcode,website,phone,featured))
        connection.commit()
    def get(id):
        query = "SELECT * from venue WHERE id = " + str(id)
        cursor.execute(query)
        venue = cursor.fetchall()
        return venue

    def table():
        venueTableSQL ="""
            CREATE TABLE "venue" (
                "id" integer NOT NULL PRIMARY KEY,
                "name" varchar(100) NOT NULL,
                "details" text,
                "address" varchar(255),
                "town" varchar(50),
                "postcode" varchar(10),
                "website" varchar(200),
                "phone" integer,
                "featured" bool NOT NULL
            );
            """
        cursor.execute(venueTableSQL)