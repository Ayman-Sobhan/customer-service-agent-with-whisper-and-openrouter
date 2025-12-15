import sqlite3

# --- Create table (run safely every time) ---
with sqlite3.connect("my.db") as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        call_id TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)


# --- Insert memory ---
def add_memory(conn, call_id, role, content):
    sql = """
    INSERT INTO memories (call_id, role, content)
    VALUES (?, ?, ?)
    """
    cur = conn.cursor()
    cur.execute(sql, (call_id, role, content))
    conn.commit()
    return cur.lastrowid


# --- Test run ---
if __name__ == "__main__":
    with sqlite3.connect("my.db") as conn:
        memory_id = add_memory(
            conn, call_id="call_123", role="user", content="Hello, my laptop is broken"
        )
        print("Inserted row id:", memory_id)
