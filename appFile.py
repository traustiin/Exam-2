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

# Function to display questions for a selected category
def display_questions(category):
    cursor.execute(f"SELECT * FROM {category}")
    questions = cursor.fetchall()
    if questions:
        print(f"Questions for {category}:")
        for question, answer in questions:
            print(f"Question: {question}")
            print(f"Answer: {answer}\n")
    else:
        print("No questions found for the selected category.")

# Function to display main menu
def display_menu():
    print("Quiz Bowl Application")
    print("1. Business Ethics")
    print("2. Business Data Management")
    print("3. Business Communication")
    print("4. Principles of Macro")
    print("5. Business App Development")
    print("6. Exit")

# Function to retrieve table names
def get_table_names():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    return [name[0] for name in table_names]

# Function to play the Quiz Bowl
def play_quiz_bowl():
    print("Welcome to Quiz Bowl!")
    
    while True:
        display_menu()
        choice = input("Enter the number of the category you want to play (or '6' to exit): ")

        if choice == '6':
            print("Exiting the Quiz Bowl.")
            break
        
        try:
            choice = int(choice)
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        selected_table = get_table_names()[choice - 1]
        display_questions(selected_table)

# Main function
def main():
    play_quiz_bowl()
    conn.close()

if __name__ == "__main__":
    main()
