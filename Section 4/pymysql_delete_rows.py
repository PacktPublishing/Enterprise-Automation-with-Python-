# import the pymysql module

import pymysql

# Code for creating a connection object

databaseServer = "127.0.0.1"

databaseUser = "root"

databaseUserPwd = ""

databaseName = "packt_database"

databaseCharSet = "utf8mb4"

dbConnection = pymysql.connect(host=databaseServer,

                               user=databaseUser,

                               password=databaseUserPwd,

                               db=databaseName,

                               charset=databaseCharSet,

                               autocommit=True)

try:

    # Code for  creating cursor from database connection

    cursorInstance = dbConnection.cursor()

    # SQL statement for deleting rows from a table matching a criteria

    sqlDeleteRows = "Delete from SuperEmployee where id=1"

    # using the cursor delete a set of rows from the table

    cursorInstance.execute(sqlDeleteRows)

    # Check if there are any existing items with expired status

    sqlSelectRows = "select * from SuperEmployee"

    # Execute the SQL query

    cursorInstance.execute(sqlSelectRows)

    # Fetch all the rows using cursor object

    itemRows = cursorInstance.fetchall()

    # print all the remaining rows after deleting the rows with status as "expired"

    for item in itemRows:
        print(item)


except Exception as ex:

    print("Exception occured: %s" % ex)

finally:

    dbConnection.close()