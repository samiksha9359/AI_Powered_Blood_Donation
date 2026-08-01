import sqlite3

conn = sqlite3.connect("blood_donation.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM blood_stock")

conn.commit()
conn.close()
 
print("Blood stock cleared successfully!")