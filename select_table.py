import sqlite3

con = sqlite3.connect("test_database_1")
cur = con.cursor()

# How would we do this dynamically? We don't, we would commit to the target currencies when making a database. 
# So we are committing to these target currencies!
res = cur.execute(
    """
    SELECT * FROM currencies
    """
)

print(res.fetchall())

con.close()