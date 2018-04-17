# mysql.server start
# mysql -u root
import pymysql

databaseServerIP = "127.0.0.1"

databaseUserName = "root"

databaseUserPassword = ""

newDatabaseName = "packt_database"

charSet = "utf8mb4"

cursorType = pymysql.cursors.DictCursor

connectionInstance = pymysql.connect(host=databaseServerIP,
                                     user=databaseUserName,
                                     password=databaseUserPassword,
                                     charset=charSet,
                                     cursorclass=cursorType)

try:

    cursorInstance = connectionInstance.cursor()

    sqlStatement = "CREATE DATABASE " + newDatabaseName

    cursorInstance.execute(sqlStatement)

    sqlQuery = "SHOW DATABASES"

    cursorInstance.execute(sqlQuery)

    databaseList = cursorInstance.fetchall()

    for database in databaseList:
        print(database)


except Exception as e:

    print("Exception occurred:{}".format(e))


finally:

    connectionInstance.close()
