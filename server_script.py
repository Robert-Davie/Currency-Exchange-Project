import sqlite3
import rq_scheduler


try:
    import create_database
except sqlite3.OperationalError:
    pass

from select_table import select

select()

