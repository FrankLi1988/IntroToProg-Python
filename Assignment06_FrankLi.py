""" Title: Assignment06

# In this assignment, you learn about additional programming tools and techniques. Course assignments help you learn
# through reading, watching demonstrations, performing programming in Python, and reflecting on what you learned
# through writing.

# Change Log: (Frank Li; Aug 05, 2026; homework for Model 06: Assignment06)

#  8/05/2026 Created script

"""
import json

# ------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------

MENU: str = '''
---- Course Registration Program ----
Select from the following menu:
1. Register a Student for a Course
2. Show current data
3. Save data to a file
4. Exit the program
-----------------------------------------
'''

FILE_NAME: str = "Enrollments.json"

# ------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------

students: list = []
menu_choice: str = ""


# ------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------

class FileProcessor:
    """
    Handles reading and writing student registration
    data to and from a JSON file.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads student registration data from a JSON file.
        """

        file = None

        try:
            file = open(file_name, "r")
            student_data.clear()
            student_data.extend(json.load(file))

        except Exception as e:
            IO.output_error_messages(
                "There was a problem reading the file.", e)

        finally:
            if file is not None and not file.closed:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes student registration data to a JSON file.
        """

        file = None

        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=4)

            print("\nData successfully saved.\n")
            IO.output_student_courses(student_data)

        except Exception as e:
            IO.output_error_messages(
                "There was a problem writing the file.", e)

        finally:
            if file is not None and not file.closed:
                file.close()


class IO:
    """
    Handles all user input and output.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays friendly and technical error messages.
        """

        print("\nError:")
        print(message)

        if error is not None:
            print("-- Technical Error Message --")
            print(error.__doc__)
            print(error)

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu.
        """

        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        Gets the user's menu choice.
        """

        return input("Enter your choice: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Displays all student registrations.
        """

        print("-" * 50)

        if len(student_data) == 0:
            print("No registrations found.")
        else:
            for student in student_data:
                print(
                    f'{student["FirstName"]}, '
                    f'{student["LastName"]}, '
                    f'{student["CourseName"]}'
                )

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompts the user to enter student registration data.
        """

        try:

            first_name = input("Enter student's first name: ")

            if not first_name.isalpha():
                raise ValueError(
                    "First name should contain letters only.")

            last_name = input("Enter student's last name: ")

            if not last_name.isalpha():
                raise ValueError(
                    "Last name should contain letters only.")

            course_name = input("Enter course name: ")

            row = {
                "FirstName": first_name,
                "LastName": last_name,
                "CourseName": course_name
            }

            student_data.append(row)

            print(
                f"\nRegistered {first_name} {last_name} for {course_name}\n")

        except Exception as e:
            IO.output_error_messages(
                "There was a problem entering data.", e)


# ------------------------------------------------------------------
# Main Program
# ------------------------------------------------------------------

FileProcessor.read_data_from_file(FILE_NAME, students)

while True:

    IO.output_menu(MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":

        IO.input_student_data(students)

    elif menu_choice == "2":

        IO.output_student_courses(students)

    elif menu_choice == "3":

        FileProcessor.write_data_to_file(FILE_NAME, students)

    elif menu_choice == "4":

        print("Program Ended")
        break

    else:

        print("Please select 1, 2, 3, or 4.")