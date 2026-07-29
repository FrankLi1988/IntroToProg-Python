""" Title: Assignment05

# In this assignment, you learn about additional programming tools and techniques. Course assignments help you learn
# through reading, watching demonstrations, performing programming in Python, and reflecting on what you learned
# through writing.

# Change Log: (Frank Li; Jul 29, 2026; homework for Model 05: Assignment05)

#  7/29/2026 Created script

"""

import json

# -----------------------------

# Constants

# -----------------------------

MENU: str = """

---- Course Registration Program ----

Select from the following menu:

1. Register a Student for a Course

2. Show current data

3. Save data to a file

4. Exit the program

-----------------------------------------

"""

FILE_NAME: str = "Enrollments.json"

# -----------------------------

# Variables

# -----------------------------

student_first_name: str = ""

student_last_name: str = ""

course_name: str = ""

file = None

menu_choice: str = ""

student_data: dict = {}

students: list = []

# -----------------------------

# Read existing data

# -----------------------------

try:

    file = open(FILE_NAME, "r")

    students = json.load(file)

    file.close()



except FileNotFoundError:

    print("The enrollment file was not found.")

    students = []



except json.JSONDecodeError:

    print("The enrollment file contains invalid data.")

    students = []



except Exception as e:

    print("An error occurred while reading the file.")

    print(e)

# -----------------------------

# Main Program

# -----------------------------

while True:

    print(MENU)

    menu_choice = input("Enter your menu choice: ")

    # -------------------------

    # Register Student

    # -------------------------

    if menu_choice == "1":

        # First Name

        while True:

            try:

                student_first_name = input("Enter student's first name: ").strip()

                if student_first_name == "":
                    raise ValueError("First name cannot be blank.")

                break



            except ValueError as e:

                print(e)

        # Last Name

        while True:

            try:

                student_last_name = input("Enter student's last name: ").strip()

                if student_last_name == "":
                    raise ValueError("Last name cannot be blank.")

                break



            except ValueError as e:

                print(e)

        # Course Name

        while True:

            try:

                course_name = input("Enter course name: ").strip()

                if course_name == "":
                    raise ValueError("Course name cannot be blank.")

                break



            except ValueError as e:

                print(e)

        student_data = {

            "FirstName": student_first_name,

            "LastName": student_last_name,

            "CourseName": course_name

        }

        students.append(student_data)

        print("\nStudent successfully registered.\n")



    # -------------------------

    # Show Current Data

    # -------------------------

    elif menu_choice == "2":

        if len(students) == 0:

            print("\nNo enrollment data available.\n")

        else:

            print("\nCurrent Enrollment Data")

            print("-" * 40)

            for row in students:
                print(f"{row['FirstName']}, {row['LastName']}, {row['CourseName']}")

            print()



    # -------------------------

    # Save Data

    # -------------------------

    elif menu_choice == "3":

        try:

            file = open(FILE_NAME, "w")

            json.dump(students, file, indent=4)

            file.close()

            print("\nData saved successfully.\n")

            print("Current file contents:")

            for row in students:
                print(f"{row['FirstName']}, {row['LastName']}, {row['CourseName']}")

            print()



        except Exception as e:

            print("An error occurred while writing the file.")

            print(e)



    # -------------------------

    # Exit Program

    # -------------------------

    elif menu_choice == "4":

        print("\nThank you for using the Course Registration Program.")

        print("Program ended.")

        break



    # -------------------------

    # Invalid Menu Choice

    # -------------------------

    else:

        print("\nPlease enter a valid menu option (1-4).\n")