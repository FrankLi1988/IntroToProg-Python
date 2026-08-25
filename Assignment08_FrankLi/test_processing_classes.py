# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Test Processing Classes
# Description: Unit tests for Employee Ratings file processing.
# ChangeLog: (Who, When, What)
#   Frank Li,08/21/2026,Created processing tests for Assignment08
# ------------------------------------------------------------------------------------------------- #

import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from data_classes import Employee
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    """Test FileProcessor JSON read and write functions."""

    def test_write_and_read(self):
        """Test saving and loading Employee objects."""
        employees = [
            Employee("John", "Smith", "2026-08-19", 5),
            Employee("Mary", "Jones", "2026-08-20", 4)
        ]

        with tempfile.TemporaryDirectory() as folder:
            file_name = str(Path(folder) / "EmployeeRatings.json")

            FileProcessor.write_employee_data_to_file(
                file_name,
                employees
            )

            with open(file_name, "r") as file:
                raw_data = json.load(file)

            self.assertEqual(len(raw_data), 2)
            self.assertEqual(raw_data[0]["FirstName"], "John")
            self.assertEqual(raw_data[0]["ReviewRating"], 5)

            loaded = []
            FileProcessor.read_employee_data_from_file(
                file_name,
                loaded,
                Employee
            )

            self.assertEqual(len(loaded), 2)
            self.assertIsInstance(loaded[0], Employee)
            self.assertEqual(loaded[0].review_date, date(2026, 8, 19))
            self.assertEqual(loaded[1].review_rating, 4)


if __name__ == "__main__":
    unittest.main()
