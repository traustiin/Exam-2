import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Function to retrieve table names
def get_table_names():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    return [name[0] for name in table_names]

# Function to retrieve all data from a table
def get_table_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    table_data = cursor.fetchall()
    return table_data

# Get and display table names
print("List of Table Names:")
for name in get_table_names():
    print(name)

# Get and display data from each table
for table_name in get_table_names():
    print(f"\nData from Table: {table_name}")
    table_data = get_table_data(table_name)
    for row in table_data:
        print(row)

# Close connection
conn.close()