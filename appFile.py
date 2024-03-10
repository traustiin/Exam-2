import sqlite3

# Color codes
GREEN = '\033[92m'  # Green
RED = '\033[91m'    # Red
RESET = '\033[0m'   # Reset color

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

def print_colored(text, color):
    """Function to print text in the specified color."""
    print(color + text + RESET)

# Ask user to select a category
print("Which of the following categories would you like questions on?")
print("1. Business Ethics")
print("2. Business Data MGMT")
print("3. Business Communication")
print("4. Principles of Macro")
print("5. Business App Development")
userDecisionCategory = input("Enter the number of the category: ")

# Define a function to handle questions for a specific category
def handle_category(category_table):
    cursor.execute(f"SELECT * FROM {category_table}")
    records = cursor.fetchall()

    # This will cycle through the questions in the table
    for record in records:
        question = record[1]
        correct_answer = record[2]
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print_colored("Correct!", GREEN)
        else:
            print_colored("Incorrect. The correct answer is:", RED)
            print(correct_answer)

# Handle user's choice of category
if userDecisionCategory == "1":
    handle_category("Business_Ethics")
elif userDecisionCategory == "2":
    handle_category("Business_Data_MGMT")
elif userDecisionCategory == "3":
    handle_category("Business_Communication")
elif userDecisionCategory == "4":
    handle_category("Principles_of_Macro")
elif userDecisionCategory == "5":
    handle_category("Business_App_Development")
else:
    print("Invalid category selection. Please enter a number between 1 and 5.")
