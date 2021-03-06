import pymongo
import sys
import time
from datetime import datetime
import logging

def log():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s <--> %(name)s <--> %(message)s')
    logger = logging.getLogger(__name__)
    return logger

def con(logger):
    log = logger
    '''
    Provides the URL to connect Python to Mongodb using Pymongo. If the mongo server is local you can use the
    following string -- "conn_str = "mongodb://<user>:<password>@localhost:<the port that the server is listening to>
    '''
    conn_str = "mongodb://UsvEr4VX6ShZRsqW:4tYwbrdXJYpS74TZ@localhost:27017"
    # Creates a connection using pymongo.MongoClient
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

    # Checks if the connection was successfully. If not, it exits the program and shows the error.
    try:
        log.info(client.server_info())
    except Exception as e:
        log.info(e)
        log.info("Unable to connect.")
        sys.exit(-1)

    return client


def data(connection,logger):
    log = logger
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection('employees')
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

    try:
        db_employee.insert_many([empl_1,empl_2,empl_3,empl_4,empl_5,empl_6,empl_7,empl_8,empl_9,empl_10])
    except Exception as e:
        log.critical(e)
        log.critical("-----EXITING-----")
        sys.exit(-1)


def timestamp(logger):
    log = logger
    #Using some prints as loggers to show the UNIX time and convert it to different time formats:
    timestamp = int(time.time())
    log.info("This is the UNIX timestamp: " + str(timestamp))
    Format = datetime.fromtimestamp(timestamp)
    log.info("See the conversion for the UNIX timestamps from the documents down bellow: ")



def format(connection, logger):
    log = logger
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    # Conversion of UNIX to romanian date format, printing it and updating it to the collections
    format_ro = time.strftime("%d/%m/%Y, %H:%M:%S")
    log.info(format_ro + " --Ro Format")
    for employee in db_employee.find():
        db_employee.update_many({}, {"$set": {"ro_time": format_ro}})

    # Conversion of UNIX to american date format, printing it and updating it to the collections
    format_us = time.strftime("%m-%d-%Y, %H:%M:%S")
    log.info(format_us + " --Us Format")
    for employee in db_employee.find():
        db_employee.update_many({}, {"$set": {"us_time": format_us}})

    # Conversion of UNIX to british date format, printing it and updating it to the collections
    format_uk = time.strftime("%d/%m/%Y, %H:%M:%S")
    log.info(format_uk + " --Uk Format")
    for employee in db_employee.find():
        db_employee.update_many({}, {"$set": {"uk_time": format_uk}})

    log.info("Updating the documents with the specified formats....\n Please wait!")


def iterate(connection, logger):
    log = logger
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    #Iterates through the documents
    for employee in db_employee.find():
        log.info(employee)
    log.info("Docs listed with succes!")


def delete_by_age(connection,parameter, logger):
    log = logger
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    log.info("Preparing to delete the documents with the employees that have the age bigger than {}....\n".format(parameter))
    # Deletes the documents whose "age" key has values greater than 30
    for employee in db_employee.find():
        db_employee.delete_many({"age": {"$gt": int(parameter)}})
    log.info("Task finished!Docs deleted")


def sort(connection, parameter, logger):
    log = logger
    client = connection
    # Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
    db = client.get_database("employee_list")
    # Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
    db_employee = db.get_collection("employees")
    for employee in db_employee.find({}).sort(parameter):
        log.info(employee)
    log.info("Task finished...\n Exiting...")



logger = log()
connect = con(logger)
data(connect, logger)
timestamp(logger)
format(connect, logger)
iterate(connect, logger)
delete_by_age(connect, 30, logger)
sort(connect, 'age', logger)
