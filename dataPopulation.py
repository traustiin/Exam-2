import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Define a function to add data to a table
def add_data(table_name, data):
    for question, answer in data:
        cursor.execute(f'''INSERT INTO {table_name} (question, answer) VALUES (?, ?)''', (question, answer))

# Generate questions and answers (Example data)
strategic_management_data = [
    ("What is SWOT analysis?", "SWOT analysis is a strategic planning technique used to help a person or organization identify strengths, weaknesses, opportunities, and threats related to business competition or project planning."),
    ("Define competitive advantage.", "Competitive advantage refers to the attributes that allow a company to outperform its competitors."),
    # Add more questions and answers here...
]

# Add data to the tables
add_data('Strategic_Management', strategic_management_data)
# Add data for other categories similarly...

# Commit changes and close connection
conn.commit()
conn.close()
