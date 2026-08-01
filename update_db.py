import sqlite3

conn = sqlite3.connect("blood_donation.db")
cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE blood_requests
    ADD COLUMN email TEXT
    """)
    conn.commit()
    print("✅ Email column added successfully!")

except Exception as e:
    print(e)

conn.close()