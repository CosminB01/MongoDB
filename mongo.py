import pymongo
import sys
import time
from datetime import datetime
#import logging

'''
def log(log):
    log = logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')
TODO
'''

def con():
    '''
    Provides the URL to connect Python to Mongodb using Pymongo. If the mongo server is local you can use the
    following string -- "conn_str = "mongodb://<user>:<password>@localhost:<the port that the server is listening to>
    '''

    conn_str = "mongodb://UsvEr4VX6ShZRsqW:4tYwbrdXJYpS74TZ@localhost:27017"

    # Creates a connection using pymongo.MongoClient
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

    # Checks if the connection was succesfully. If not, it exits the program and shows the error.
    try:
        print(client.server_info())
    except Exception as e:
        print(e)
        print("Unable to connect.")
        sys.exit(-1)

    return client

def timestamp(connection):
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    #Using some prints as loggers to show the UNIX time and convert it to different time formats:
    timestamp = int(time.time())
    print("This is the UNIX timestamp: " + str(timestamp))
    Format = datetime.fromtimestamp(timestamp)
    print("See the conversion for the UNIX timestamps from the documents down bellow: ")
    print('TIMESTAMP')


def format(connection):
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    # Conversion of UNIX to romanian date format, printing it and updating it to the collections
    Format = time.strftime("%d/%m/%Y, %H:%M:%S")
    print(Format + " --Ro Format")
    for employee in db_employee.find():
        db_employee.update_many({}, {"$set": {"ro_time": Format}})

    # Conversion of UNIX to american date format, printing it and updating it to the collections
    Format = time.strftime("%m-%d-%Y, %H:%M:%S")
    print(Format + " --Us Format")
    for employee in db_employee.find():
        db_employee.update_many({}, {"$set": {"us_time": Format}})

    # Conversion of UNIX to british date format, printing it and updating it to the collections
    Format = time.strftime("%d/%m/%Y, %H:%M:%S")
    print(Format + " --Uk Format")
    for employee in db_employee.find():
        db_employee.update_many({}, {"$set": {"uk_time": Format}})

    print("Updating the documents with the specified formats....\n Please wait!")

def iterate(connection):
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    #Iterates through the documents
    for employee in db_employee.find():
        print(employee)
    print("Docs listed with succes!")

def delete(connection):
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    print("Preparing to delete the documents with the employees that have the age bigger than 30....\n")
    # Deletes the documents whose "age" key has values greater than 30
    for employee in db_employee.find():
        db_employee.delete_many({"age": {"$gt": 30}})
    print("Task finished!Docs deleted")

def sort(connection):
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    # Iterates through the documents and sorts them by age (ascending
    for employee in db_employee.find({}).sort("age"):
        print(employee)
    print("Task finished...\n Exiting...")

connect = con()
def data(connection):
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    empl_1 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0001",
            "name" : "Mike",
            "age" : 23
        }
    empl_2 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0002",
            "name" : "Sarah",
            "age" : 31
        }
    empl_3 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0003",
            "name" : "John",
            "age" : 27
        }
    empl_4 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0004",
            "name" : "Beatrice",
            'age' : 33
        }
    empl_5 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0005",
            "name" : "Steve",
            "age" : 21
        }
    empl_6 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0006",
            "name" : "Anna",
            "age" : 30
        }
    empl_7 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0007",
            "name" : "Andy",
            "age" : 29
        }
    empl_8 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0008",
            "name" : "Janna",
            "age" : 40
        }
    empl_9 = {
            "timestamp_UNIX" : int(time.time()),

            "_id" : "empl0009",
            "name" : "Kevin",
            "age" : 25
        }
    empl_10 = {
            "timestamp_UNIX" : int(time.time()),
            "_id" : "empl0010",
            "name" : "Senna",
            "age" : 19
        }
    #Inserts the dictionaries as db collections
    db_employee.insert_many([empl_1, empl_2, empl_3, empl_4, empl_5, empl_6, empl_7, empl_8, empl_9, empl_10])


timestamp(connect)
format(connect)
iterate(connect)
delete(connect)
sort(connect)











