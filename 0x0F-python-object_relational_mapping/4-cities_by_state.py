#!/usr/bin/python3
"""states models
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON states.id = cities.state_id \
    ORDER BY cities.id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
