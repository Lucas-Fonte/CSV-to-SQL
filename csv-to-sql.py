from utils.helpers import (
    csvFileToArrayOfDictionaries,
    connectToDatabase,
    createTable,
    uploadDictionariesToDatabase,
    printData
)

FILE_PATH = './data/data.csv'
DATABASE_CONFIG = 'example.db'

def runCsvToSQL():
    csvAsDictionaries = csvFileToArrayOfDictionaries(FILE_PATH)

    print(csvAsDictionaries)

    database = connectToDatabase(DATABASE_CONFIG)
    createTable(database)
    uploadDictionariesToDatabase(csvAsDictionaries, database)
    printData(database)

runCsvToSQL()


