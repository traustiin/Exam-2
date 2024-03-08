import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# SQL script to remove old tables
sql_script = """
    -- Drop the tables created for the Quiz Bowl application
    DROP TABLE IF EXISTS Strategic_Management;
    DROP TABLE IF EXISTS Digital_Marketing;
    DROP TABLE IF EXISTS Personal_Sales;
    DROP TABLE IF EXISTS Information_Systems;
    DROP TABLE IF EXISTS Finance;
"""

# Execute the SQL script
cursor.executescript(sql_script)

# Commit changes and close connection
conn.commit()
conn.close()

print("Old tables removed successfully.")

