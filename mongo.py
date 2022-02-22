import pymongo
import sys
import time

'''
Provides the URL to connect Python to Mongodb using Pymongo. If the mongo server is local you can use the
following string -- "conn_str = "mongodb://<user>:<password>@localhost:<the port that the server is listening to>
'''
conn_str = "mongodb://root:password@localhost:27017"

#Creates a connection using pymongo.MongoClient
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

#Checks if the connection was succesfully. If not, it exits the program and shows the error.
try:
    print(client.server_info())
except Exception as e:
    print(e)
    print("Unable to connect.")
    sys.exit(-1)

'''
#UNIX timestamp
now = int(time.time())

timestamp_ro = time.strftime("%d/%m/%Y")

timestamp_uk = time.strftime("%d/%m/%Y")

timestamp_us = time.strftime("%m-%d-%Y")
'''



#Creates the database named 'employee_list' -- db = client.get_database("your_database_name")
db = client.get_database("employee_list")

#Creates a collection named 'employees' in the 'employees_list' -- collection_name = dbname["your_collection_name"]
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
    "age" : "21"
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


db_employee.insert_many([empl_1, empl_2, empl_3, empl_4, empl_5, empl_6, empl_7, empl_8, empl_9, empl_10])
#log.show_log = ("INF", empl_1, "mongo.py", 0)
