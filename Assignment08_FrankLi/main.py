""" Title: Assignment08

# In this assignment, you learn about additional programming tools and techniques. Course assignments help you learn
# through reading, watching demonstrations, performing programming in Python, and reflecting on what you learned
# through writing.

# Change Log: (Frank Li; Aug 20, 2026; homework for Model 08: Assignment08)

#  8/20/2026 Created script

"""
from data_classes import Employee
from processing_classes import FileProcessor
from presentation_classes import IO


FILE_NAME: str = "EmployeeRatings.json"

MENU: str = """
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
"""


employees: list = []
menu_choice = ''


employees = FileProcessor.read_employee_data_from_file(
    file_name=FILE_NAME,
    employee_data=employees,
    employee_type=Employee
)


while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.output_employee_data(employee_data=employees)
        continue

    elif menu_choice == "2":
        employees = IO.input_employee_data(
            employee_data=employees,
            employee_type=Employee
        )
        continue

    elif menu_choice == "3":
        FileProcessor.write_employee_data_to_file(
            file_name=FILE_NAME,
            employee_data=employees
        )
        print(f"Data was saved to the {FILE_NAME} file.")
        continue

    elif menu_choice == "4":
        break

print("Program Ended")
