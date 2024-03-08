import sqlite3
import random

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Function to get a random question from a table
def get_random_question(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    random_row = random.choice(rows)
    return random_row

# Function to play the Quiz Bowl
def play_quiz_bowl():
    print("Welcome to Quiz Bowl!")
    print("Choose a category:")
    table_names = get_table_names()
    for index, name in enumerate(table_names, 1):
        print(f"{index}. {name}")
    choice = int(input("Enter the number of the category you want to play: "))
    selected_table = table_names[choice - 1]
    question, answer = get_random_question(selected_table)[1:]
    print(f"\nCategory: {selected_table.replace('_', ' ')}")
    print("Question:", question)
    user_answer = input("Your answer: ").strip().lower()
    if user_answer == answer.lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", answer)

# Function to retrieve table names
def get_table_names():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    return [name[0] for name in table_names]

# Main function
def main():
    play_quiz_bowl()
    conn.close()

if __name__ == "__main__":
    main()