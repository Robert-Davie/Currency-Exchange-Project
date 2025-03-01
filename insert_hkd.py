import sqlite3

con = sqlite3.connect("test_database_1")
cur = con.cursor()

# added hkd to the table
cur.execute(
    """
    ALTER TABLE currencies ADD COLUMN hkd;
    """
)
con.close()
