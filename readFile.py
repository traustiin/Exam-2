import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()



# Function to retrieve table names
def get_table_names():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    return [name[0] for name in table_names]
print("Table Names:",get_table_names(),"\n\n")

# Function to retrieve all data from a table
def get_table_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    table_data = cursor.fetchall()
    print(table_name,table_data)
get_table_data("Business_Ethics")
get_table_data("Business_Data_MGMT")
get_table_data("Business_Communication")
get_table_data("Principles_of_Macro")
get_table_data("Business_App_Development")

