# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Data Classes
# Description: Contains Person and Employee data classes for the Employee Ratings application.
# ChangeLog: (Who, When, What)
#   Frank Li,08/21/2026,Created data classes for Assignment08
# ------------------------------------------------------------------------------------------------- #

from datetime import date


class Person:
    """Represents basic person information."""

    def __init__(self, first_name: str = "", last_name: str = ""):
        """Initialize a Person object with a first and last name."""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self) -> str:
        """Return the person's first name."""
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """Set the first name after simple validation."""
        if not isinstance(value, str):
            raise TypeError("First name must be a string.")
        if value == "":
            self.__first_name = value
        elif value.isalnum():
            self.__first_name = value
        else:
            raise ValueError("The first name should contain only letters and numbers.")

    @property
    def last_name(self) -> str:
        """Return the person's last name."""
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """Set the last name after simple validation."""
        if not isinstance(value, str):
            raise TypeError("Last name must be a string.")
        if value == "":
            self.__last_name = value
        elif value.isalnum():
            self.__last_name = value
        else:
            raise ValueError("The last name should contain only letters and numbers.")

    def __str__(self) -> str:
        """Return person data as comma-separated values."""
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """Represents an employee and the employee's performance review."""

    def __init__(
        self,
        first_name: str = "",
        last_name: str = "",
        review_date: date = date(1900, 1, 1),
        review_rating: int = 3
    ):
        """Initialize an Employee object."""
        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self) -> date:
        """Return the review date as a datetime.date object."""
        return self.__review_date

    @review_date.setter
    def review_date(self, value):
        """Set the review date after validating YYYY-MM-DD."""
        if isinstance(value, date):
            self.__review_date = value
        elif isinstance(value, str):
            try:
                self.__review_date = date.fromisoformat(value)
            except ValueError:
                raise ValueError(
                    "Incorrect data format, should be YYYY-MM-DD"
                )
        else:
            raise TypeError(
                "Review date must be a datetime.date or YYYY-MM-DD string."
            )

    @property
    def review_rating(self) -> int:
        """Return the employee review rating."""
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        """Set the review rating after validating values 1 through 5."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Review rating must be an integer from 1 through 5.")
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5.")

    def __str__(self) -> str:
        """Return employee data as comma-separated values."""
        return (
            f"{self.first_name},{self.last_name},"
            f"{self.review_date.isoformat()},{self.review_rating}"
        )
