# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Presentation Classes
# Description: Contains presentation-layer input and output functions.
#
#   Frank Li,08/19/2026,Created presentation classes for Assignment08
# ------------------------------------------------------------------------------------------------- #


class IO:
    """Manages employee input and application output."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Display a custom error message and optional technical information."""
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """Display the application menu."""
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """Get and validate a menu choice from the user."""
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise ValueError("Please choose only 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages(
                message="There was a problem with your menu choice.",
                error=e
            )
        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """Display employee review data and rating descriptions."""
        try:
            print()
            print("-" * 50)

            if not employee_data:
                print("No employee rating data found.")
            else:
                for employee in employee_data:
                    if employee.review_rating == 5:
                        rating_text = "Leading"
                    elif employee.review_rating == 4:
                        rating_text = "Strong"
                    elif employee.review_rating == 3:
                        rating_text = "Solid"
                    elif employee.review_rating == 2:
                        rating_text = "Building"
                    else:
                        rating_text = "Not Meeting Expectations"

                    print(
                        f"{employee.first_name} {employee.last_name} "
                        f"is rated as {employee.review_rating} ({rating_text}) "
                        f"on {employee.review_date.isoformat()}"
                    )

            print("-" * 50)
            print()
        except Exception as e:
            IO.output_error_messages(
                message="There was a problem displaying employee data.",
                error=e
            )

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        """Prompt for employee name, review date, and review rating."""
        try:
            employee_object = employee_type()

            employee_object.first_name = input(
                "What is the employee's first name? "
            )
            employee_object.last_name = input(
                "What is the employee's last name? "
            )
            employee_object.review_date = input(
                "What is their review date (YYYY-MM-DD)? "
            )
            employee_object.review_rating = int(
                input("What is their review rating (1-5)? ")
            )

            employee_data.append(employee_object)

            print()
            print("Employee review data was added:")
            print(employee_object)
            print()

        except ValueError as e:
            IO.output_error_messages(
                message="That value is not the correct type of data.",
                error=e
            )
        except Exception as e:
            IO.output_error_messages(
                message="There was a problem entering employee data.",
                error=e
            )

        return employee_data
