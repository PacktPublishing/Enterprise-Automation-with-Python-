# import the mysql client for python

import pymysql

# Create a connection object

dbServerName = "127.0.0.1"

dbUser = "root"

dbPassword = ""

dbName = "packt_database"  # created by create_db.py

charSet = "utf8mb4"

cursorType = pymysql.cursors.DictCursor

connectionObject = pymysql.connect(host=dbServerName,
                                   user=dbUser,
                                   password=dbPassword,
                                   db=dbName,
                                   charset=charSet,
                                   cursorclass=cursorType)

try:

    # Create a cursor object

    cursorObject = connectionObject.cursor()

    # SQL query string

    sqlQuery = "CREATE TABLE " \
               "Employee(id int, " \
               "LastName varchar(32), " \
               "FirstName varchar(32), " \
               "DepartmentCode int)"

    # Execute the sqlQuery

    cursorObject.execute(sqlQuery)

    # SQL query string

    sqlQuery = "show tables"

    # Execute the sqlQuery

    cursorObject.execute(sqlQuery)

    # Fetch all the rows

    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

except Exception as e:

    print("Exception occurred:{}".format(e))

finally:

    connectionObject.close()
