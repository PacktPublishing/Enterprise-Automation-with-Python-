# import the pymysql module

import pymysql

# Making connection to the MySQL Server


hostIP = "127.0.0.1"

userName = "root"

userPassword = ""

database = "packt_database"

charset = "utf8mb4"

cursorType = pymysql.cursors.DictCursor

con = pymysql.connect(host=hostIP,

                      user=userName,

                      password=userPassword,

                      db=database,

                      charset=charset,

                      cursorclass=cursorType,

                      autocommit=True)

try:

    # Creation of cursor object

    cursorObject = con.cursor()

    # Alter the student table by adding one more column

    alterStatement = "ALTER TABLE SuperEmployee ADD courseid int(11);"

    # Execute the SQL ALTER statement

    cursorObject.execute(alterStatement)

    # Verify the new schema by issuing a DESCRIBE statament

    descibeStatement = "DESC SuperEmployee"

    # Execute the SQL SELECT query

    cursorObject.execute(descibeStatement)

    # Fetch the updated row

    columns = cursorObject.fetchall()

    # Print the updated row...

    for column in columns:
        print(column)


except Exception as e:

    print("Exeception occured:{}".format(e))


finally:

    con.close()