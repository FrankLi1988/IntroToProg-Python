""" Title: Assignment07

# In this assignment, you learn about additional programming tools and techniques. Course assignments help you learn
# through reading, watching demonstrations, performing programming in Python, and reflecting on what you learned
# through writing.

# Change Log: (Frank Li; Aug 10, 2026; homework for Model 06: Assignment07)

#  8/10/2026 Created script

"""

import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program2
-----------------------------------------
'''

FILE_NAME: str = "Enrollments.json"


# Define the Data Variables
students: list = []       # A list of Student objects
menu_choice: str = ''     # Holds the choice made by the user


# ------------------------------------------------------------------------------------------ #
# Data Classes
# ------------------------------------------------------------------------------------------ #

class Person:
    """
    A data class that stores a person's first and last name.

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    def __init__(self, first_name: str = '', last_name: str = ''):
        """
        Initializes a Person object.

        :param first_name: The person's first name.
        :param last_name: The person's last name.
        """

        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self) -> str:
        """
        Gets the person's first name.

        :return: The first name.
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        """
        Sets the person's first name with simple validation.

        :param value: The first name.
        """

        if not isinstance(value, str):
            raise TypeError("First name must be a string.")

        if value.strip() == '':
            raise ValueError("First name cannot be empty.")

        if not value.isalpha():
            raise ValueError(
                "First name should contain letters only."
            )

        self._first_name = value.strip()

    @property
    def last_name(self) -> str:
        """
        Gets the person's last name.

        :return: The last name.
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        """
        Sets the person's last name with simple validation.

        :param value: The last name.
        """

        if not isinstance(value, str):
            raise TypeError("Last name must be a string.")

        if value.strip() == '':
            raise ValueError("Last name cannot be empty.")

        if not value.isalpha():
            raise ValueError(
                "Last name should contain letters only."
            )

        self._last_name = value.strip()

    def __str__(self) -> str:
        """
        Returns the person's first and last name
        as comma-separated values.

        :return: First name and last name.
        """

        return f"{self.first_name}, {self.last_name}"


class Student(Person):
    """
    A data class that inherits from Person and stores
    a student's course information.

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    def __init__(
            self,
            first_name: str = '',
            last_name: str = '',
            course_name: str = ''
    ):
        """
        Initializes a Student object.

        :param first_name: The student's first name.
        :param last_name: The student's last name.
        :param course_name: The student's course name.
        """

        # Call the Person constructor
        super().__init__(first_name, last_name)

        # Set course name
        self.course_name = course_name

    @property
    def course_name(self) -> str:
        """
        Gets the student's course name.

        :return: The course name.
        """
        return self._course_name

    @course_name.setter
    def course_name(self, value: str):
        """
        Sets the student's course name with simple validation.

        :param value: The course name.
        """

        if not isinstance(value, str):
            raise TypeError("Course name must be a string.")

        if value.strip() == '':
            raise ValueError("Course name cannot be empty.")

        self._course_name = value.strip()

    def __str__(self) -> str:
        """
        Returns the student's information as
        comma-separated values.

        :return: First name, last name, and course name.
        """

        return (
            f"{self.first_name}, "
            f"{self.last_name}, "
            f"{self.course_name}"
        )


# ------------------------------------------------------------------------------------------ #
# Processing
# ------------------------------------------------------------------------------------------ #

class FileProcessor:
    """
    A collection of processing layer functions that work
    with JSON files.

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads data from a JSON file and converts dictionary
        rows into Student objects.

        :param file_name: Name of the file to read.
        :param student_data: List to store Student objects.
        :return: List of Student objects.
        """

        file = None

        try:
            # Open the JSON file
            file = open(file_name, "r")

            # Load dictionary rows from the JSON file
            json_students = json.load(file)

            # Clear existing Student objects
            student_data.clear()

            # Convert dictionary rows into Student objects
            for student in json_students:

                student_object = Student(
                    first_name=student["FirstName"],
                    last_name=student["LastName"],
                    course_name=student["CourseName"]
                )

                student_data.append(student_object)

        except FileNotFoundError as e:
            IO.output_error_messages(
                message="Error: The file could not be found.",
                error=e
            )

        except json.JSONDecodeError as e:
            IO.output_error_messages(
                message="Error: The file does not contain valid JSON data.",
                error=e
            )

        except Exception as e:
            IO.output_error_messages(
                message="Error: There was a problem with reading the file.",
                error=e
            )

        finally:
            # Close the file if it is open
            if file is not None and not file.closed:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Converts Student objects into dictionary rows
        and writes them to a JSON file.

        :param file_name: Name of the file to write.
        :param student_data: List of Student objects.
        :return: None
        """

        file = None

        try:
            # Create a list of dictionary rows
            json_students = []

            for student in student_data:

                student_dictionary = {
                    "FirstName": student.first_name,
                    "LastName": student.last_name,
                    "CourseName": student.course_name
                }

                json_students.append(student_dictionary)

            # Open the JSON file for writing
            file = open(file_name, "w")

            # Write dictionary rows to the file
            json.dump(json_students, file, indent=4)

            print()
            print("The following data was saved to file:")

            # Display saved data
            IO.output_student_courses(
                student_data=student_data
            )

        except Exception as e:
            message = (
                "Error: There was a problem with writing to the file.\n"
                "Please check that the file is not open by another program."
            )

            IO.output_error_messages(
                message=message,
                error=e
            )

        finally:
            # Close the file if it is open
            if file is not None and not file.closed:
                file.close()


# ------------------------------------------------------------------------------------------ #
# Presentation
# ------------------------------------------------------------------------------------------ #

class IO:
    """
    A collection of presentation layer functions that manage
    user input and output.

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(
            message: str,
            error: Exception = None
    ):
        """
        Displays custom error messages to the user.

        :param message: Custom error message.
        :param error: Exception object with technical information.
        :return: None
        """

        print()
        print(message)

        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu of choices to the user.

        :param menu: Menu text to display.
        :return: None
        """

        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        Gets a menu choice from the user.

        :return: The user's menu choice.
        """

        choice = "0"

        try:
            choice = input("Enter your menu choice number: ")

            if choice not in ("1", "2", "3", "4"):
                raise ValueError(
                    "Please choose only 1, 2, 3, or 4."
                )

        except Exception as e:
            IO.output_error_messages(
                message=e.__str__()
            )

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Displays student first name, last name, and course
        as comma-separated values.

        :param student_data: List of Student objects.
        :return: None
        """

        print("-" * 50)

        if len(student_data) == 0:
            print("No student registrations found.")
        else:
            for student in student_data:
                print(student)

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        Gets a student's first name, last name, and course name
        and creates a Student object.

        :param student_data: List of Student objects.
        :return: Updated list of Student objects.
        """

        try:
            # Get first name
            student_first_name = input(
                "Enter the student's first name: "
            )

            if not student_first_name.isalpha():
                raise ValueError(
                    "The first name should contain letters only."
                )

            # Get last name
            student_last_name = input(
                "Enter the student's last name: "
            )

            if not student_last_name.isalpha():
                raise ValueError(
                    "The last name should contain letters only."
                )

            # Get course name
            course_name = input(
                "Please enter the name of the course: "
            )

            # Create Student object
            student = Student(
                first_name=student_first_name,
                last_name=student_last_name,
                course_name=course_name
            )

            # Add Student object to list
            student_data.append(student)

            print()
            print(
                f"You have registered "
                f"{student.first_name} "
                f"{student.last_name} "
                f"for {student.course_name}."
            )

        except ValueError as e:
            IO.output_error_messages(
                message="There was a problem with the entered data.",
                error=e
            )

        except Exception as e:
            IO.output_error_messages(
                message="Error: There was a problem with your entered data.",
                error=e
            )

        return student_data


# ------------------------------------------------------------------------------------------ #
# Main Body
# ------------------------------------------------------------------------------------------ #

# Read the JSON file when the program starts
students = FileProcessor.read_data_from_file(
    file_name=FILE_NAME,
    student_data=students
)


# Present and Process the data
while True:

    # Display the menu
    IO.output_menu(menu=MENU)

    # Get menu choice
    menu_choice = IO.input_menu_choice()

    # Register a Student
    if menu_choice == "1":

        students = IO.input_student_data(
            student_data=students
        )

        continue

    # Show current data
    elif menu_choice == "2":

        IO.output_student_courses(
            student_data=students
        )

        continue

    # Save data to a file
    elif menu_choice == "3":

        FileProcessor.write_data_to_file(
            file_name=FILE_NAME,
            student_data=students
        )

        continue

    # Exit program
    elif menu_choice == "4":

        break


print("Program Ended")