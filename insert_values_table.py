import sqlite3
import API_test1

con = sqlite3.connect("test_database_1")

cur = con.cursor()

result = API_test1.main()
print(result)

cur.execute(
    """
    INSERT INTO currencies VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """, 
    (
        result["Date_from_API"],
        result["Current_Time"],
        result["gbp"],
        result["eur"],
        result["usd"],
        result["jpy"],
        result["inr"],
        result["rub"], 
    )
)

con.commit()

con.close()