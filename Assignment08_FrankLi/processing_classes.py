# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Processing Classes
# Description: Contains file-processing functions for Employee Ratings JSON data.
#
#   Frank Li,08/19/2026,Created processing classes for Assignment08
# ------------------------------------------------------------------------------------------------- #

import json
from presentation_classes import IO


class FileProcessor:
    """Reads and writes Employee Ratings JSON data."""

    @staticmethod
    def read_employee_data_from_file(
        file_name: str,
        employee_data: list,
        employee_type: object
    ):
        """Read JSON rows and convert them into Employee objects."""
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)

            employee_data.clear()

            for employee in list_of_dictionary_data:
                employee_object = employee_type()
                employee_object.first_name = employee["FirstName"]
                employee_object.last_name = employee["LastName"]
                employee_object.review_date = employee["ReviewDate"]
                employee_object.review_rating = int(employee["ReviewRating"])
                employee_data.append(employee_object)

        except FileNotFoundError as e:
            IO.output_error_messages(
                message="Error: The employee data file could not be found.",
                error=e
            )
        except json.JSONDecodeError as e:
            IO.output_error_messages(
                message="Error: EmployeeRatings.json is not valid JSON.",
                error=e
            )
        except Exception as e:
            IO.output_error_messages(
                message="Error: There was a problem reading employee data.",
                error=e
            )

        return employee_data

    @staticmethod
    def write_employee_data_to_file(
        file_name: str,
        employee_data: list
    ):
        """Convert Employee objects to dictionaries and write JSON data."""
        try:
            list_of_dictionary_data = []

            for employee in employee_data:
                employee_json = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date.isoformat(),
                    "ReviewRating": employee.review_rating
                }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=2)

        except TypeError as e:
            IO.output_error_messages(
                message="Please check that the employee data is valid JSON data.",
                error=e
            )
        except PermissionError as e:
            IO.output_error_messages(
                message="Please check the data file's read/write permission.",
                error=e
            )
        except Exception as e:
            IO.output_error_messages(
                message="Error: There was a problem writing employee data.",
                error=e
            )
