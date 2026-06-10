import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/aeromind.db")

print("AeroMind database created successfully!")

conn.close()