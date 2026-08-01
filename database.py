import sqlite3

conn = sqlite3.connect("blood_donation.db")
cursor = conn.cursor()

# ==========================
# Donors Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS donors(
    donor_id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    blood_group TEXT,
    phone TEXT UNIQUE,
    email TEXT UNIQUE,
    city TEXT,
    address TEXT,
    last_donation TEXT
)
""")

# ==========================
# Blood Requests Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS blood_requests(
    request_id TEXT PRIMARY KEY,
    request_type TEXT,
    hospital_name TEXT,
    patient_name TEXT,
    blood_group TEXT,
    units INTEGER,
    phone TEXT,
    city TEXT,
    request_date TEXT,
    status TEXT
)
""")

# ==========================
# Blood Stock Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS blood_stock(
    blood_group TEXT PRIMARY KEY,
    units INTEGER
)
""")

# Default Blood Stock
blood_groups = [
    ("A+", 0),
    ("A-", 0),
    ("B+", 0),
    ("B-", 0),
    ("AB+", 0),
    ("AB-", 0),
    ("O+", 0),
    ("O-", 0)
]

cursor.executemany("""
INSERT OR IGNORE INTO blood_stock
VALUES (?,?)
""", blood_groups)

conn.commit()
conn.close()

print("✅ Final Database Created Successfully!")