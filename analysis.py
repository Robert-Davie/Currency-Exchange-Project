import pandas as pd
import sqlite3
import matplotlib.pyplot as plt 

conn = sqlite3.connect("test_database_1")
df = pd.read_sql_query("SELECT * FROM currencies", conn)
print(df)
df.plot(x="date", y=["jpy", "inr", "rub", "hkd"])
df.plot(x="date", y=["eur", "usd"])
plt.show()
conn.close()



