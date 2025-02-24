import sqlite3

con = sqlite3.connect("test_database_1")
cur = con.cursor()

# How would we do this dynamically? We don't, we would commit to the target currencies when making a database. 
# So we are committing to these target currencies!
cur.execute(
    """
    CREATE TABLE currencies(date, access_time, gbp, eur, usd, jpy, inr, rub); 
    """
)
con.close()
