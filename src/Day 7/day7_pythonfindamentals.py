# Task 1: Create a simple journal application that allows users to input their name and daily goal, and saves it to a text file.

name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(name + " - " + goal + "\n")


# Task 2: Read the contents of the journal.txt file and display it to the user.

import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        if row[2] == "Pass":
            print(row[0])


# Task 3: Implement error handling for file operations. For example, if the user tries to open a file that doesn't exist, catch the exception and display an appropriate message.

filename = input("Enter the filename to open: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File contents:\n")
        print(content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
