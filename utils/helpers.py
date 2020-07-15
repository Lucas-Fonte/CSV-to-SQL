import sqlite3 as sqlite3
import csv as csv

def connectToDatabase(databaseConfig):
    return sqlite3.connect(databaseConfig)

def csvFileToArrayOfDictionaries(file):
    arrayOfDictionaries = []
    for row in csv.DictReader(open(file), skipinitialspace=True):
        arrayOfDictionaries.append({
            key: value for key, value in row.items()
        })
            
    return arrayOfDictionaries

def createTable(database):
    cursor = database.cursor()
    createTableSQL = ("CREATE TABLE elements (id int, name text)")

    cursor.execute(createTableSQL)

def uploadDictionariesToDatabase(dictionaries, database):
    cursor = database.cursor()

    for dicitionary in dictionaries:
        insertSQL = "INSERT INTO elements (id, name) VALUES (?, ?)"
        values = (
            dicitionary['id'], 
            dicitionary['name']
        )
        cursor.execute(insertSQL, values)

    database.commit()

def printData(database):
    cursor = database.cursor()

    selectSQL = ("SELECT * FROM elements")

    for row in cursor.execute(selectSQL):
        print(row)