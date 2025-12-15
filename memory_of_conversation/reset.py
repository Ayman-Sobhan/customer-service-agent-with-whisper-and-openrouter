import sqlite3

with sqlite3.connect("my.db") as conn:
    conn.execute("DELETE FROM memories")
    conn.commit()

print("All rows deleted from memories")
