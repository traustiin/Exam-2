import sqlite3
import random

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()




#  get question from a table
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
