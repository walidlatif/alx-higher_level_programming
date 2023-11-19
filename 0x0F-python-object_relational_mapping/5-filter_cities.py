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
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cursor = connection.cursor()
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name LIKE BINARY %s "
        "ORDER BY cities.id ASC"
        )
    cursor.execute(query, (state_name,))
    data = cursor.fetchall()

    city_names = [d[0] for d in data]
    print(", ".join(city_names))

    cursor.close()
    connection.close()
