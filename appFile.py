import sqlite3
import random

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

userDecisionCategory = input("""Which of the following categories would you like questions on?
                             1. Business Ethics
                             2. Business Data MGMT
                             3. Business Communication
                             4. Principles of Macro
                             5. Business App Development
                             """)

if userDecisionCategory == "1":
    cursor.execute("SELECT * FROM Business_Ethics")
    records = cursor.fetchall()

    #this will cycle through the questions in the table above
    for record in records:
        question = record[1]
        correct_answer = record[2]  
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)

if userDecisionCategory == "2":
    cursor.execute("SELECT * FROM Business_Data_MGMT")
    records = cursor.fetchall()

    for record in records:
        question = record[1]
        correct_answer = record[2]  
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)

if userDecisionCategory == "3":
    cursor.execute("SELECT * FROM Business_Communication")
    records = cursor.fetchall()

    for record in records:
        question = record[1]
        correct_answer = record[2]  
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)

if userDecisionCategory == "4":
    cursor.execute("SELECT * FROM Principles_of_Macro")
    records = cursor.fetchall()

    for record in records:
        question = record[1]
        correct_answer = record[2]  
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)

if userDecisionCategory == "5":
    cursor.execute("SELECT * FROM Business_App_Development")
    records = cursor.fetchall()
    
    for record in records:
        question = record[1]
        correct_answer = record[2]  
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)