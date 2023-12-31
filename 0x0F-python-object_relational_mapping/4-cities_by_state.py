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

    connection = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cursor = connection.cursor()
    query = (
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
            )
    cursor.execute(query)
    data = cursor.fetchall()

    for d in data:
        print(d)

    cursor.close()
    connection.close()
