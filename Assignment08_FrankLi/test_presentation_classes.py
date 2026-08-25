# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Test Presentation Classes
# Description: Unit tests for Employee Ratings presentation functions.
# ChangeLog: (Who, When, What)
#   Frank Li,08/20/2026,Created presentation tests for Assignment08
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

from data_classes import Employee
from presentation_classes import IO


class TestIO(unittest.TestCase):
    """Test IO presentation functions."""

    def test_menu_choice(self):
        """Test valid menu input."""
        with patch("builtins.input", return_value="2"):
            self.assertEqual(IO.input_menu_choice(), "2")

    def test_input_employee_data(self):
        """Test employee input and object creation."""
        employees = []

        with patch(
            "builtins.input",
            side_effect=["John", "Smith", "2026-08-19", "5"]
        ):
            IO.input_employee_data(employees, Employee)

        self.assertEqual(len(employees), 1)
        self.assertIsInstance(employees[0], Employee)
        self.assertEqual(employees[0].first_name, "John")
        self.assertEqual(employees[0].review_rating, 5)

    def test_output_employee_data(self):
        """Test employee data output."""
        employees = [Employee("John", "Smith", "2026-08-19", 5)]

        output = StringIO()
        with redirect_stdout(output):
            IO.output_employee_data(employees)

        self.assertIn("John Smith", output.getvalue())
        self.assertIn("Leading", output.getvalue())


if __name__ == "__main__":
    unittest.main()
