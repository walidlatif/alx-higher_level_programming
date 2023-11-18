#!/usr/bin/python3
'''
lists all states from the database
'''
if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_searched = sys.argv[4]

    connection = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
            )
    cursor = connection.cursor()
    query = "SELECT * FROM states " \
            "WHERE name LIKE BINARY '{}' " \
            "ORDER BY id ASC".format(name_searched)

    cursor.execute(query)
    data = cursor.fetchall()

    for d in data:
        print(d)

    cursor.close()
    connection.close()
