import sqlite3

def create_and_fill_db():
    conn = sqlite3.connect("dna_database.db")
    c = conn.cursor()

    # Create table with your schema
    c.execute("""
        CREATE TABLE IF NOT EXISTS dna_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            display INTEGER DEFAULT 1,
            custom_identifier TEXT
        )
    """)

    # Example pre-filled data (you can later replace this with real DNA names)
    dna_entries = [
        ("GeneA", 1, None),
        ("GeneB", 1, None),
        ("GeneC", 1, None),
        ("GeneD", 1, None),
        ("GeneE", 1, None),
    ]

    # Only fill if table is empty
    c.execute("SELECT COUNT(*) FROM dna_items")
    if c.fetchone()[0] == 0:
        c.executemany(
            "INSERT INTO dna_items (name, display, custom_identifier) VALUES (?, ?, ?)",
            dna_entries
        )
        print("Database created and pre-filled with DNA entries.")
    else:
        print("Database already has data. No refill performed.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_fill_db()