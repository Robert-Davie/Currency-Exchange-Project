import sqlite3

def select():

    con = sqlite3.connect("test_database_1")
    cur = con.cursor()

    # How would we do this dynamically? We don't, we would commit to the target currencies when making a database. 
    # So we are committing to these target currencies!
    res = cur.execute(
        """
        SELECT * FROM currencies
        """
    )
    database_result = res.fetchall()
    print(database_result)

    con.close()

    return database_result


