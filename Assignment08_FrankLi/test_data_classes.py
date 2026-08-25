# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Test Data Classes
# Description: Unit tests for Person and Employee data classes.
# ChangeLog: (Who, When, What)
#  
#   Frank Li,08/23/2026,Created data class tests for Assignment08
# ------------------------------------------------------------------------------------------------- #

import unittest
from datetime import date
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):
    """Test the Person class."""

    def test_names(self):
        """Test valid first and last names."""
        person = Person("john", "smith")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Smith")
        self.assertEqual(str(person), "John,Smith")

    def test_invalid_first_name(self):
        """Test invalid first names."""
        with self.assertRaises(ValueError):
            Person("John123", "Smith")

    def test_last_name_accepts_numbers(self):
        """Test that last names containing letters and numbers are accepted."""
        person = Person("John", "frank003")
        self.assertEqual(person.last_name, "Frank003")

    def test_invalid_last_name(self):
        """Test last names containing unsupported characters."""
        with self.assertRaises(ValueError):
            Person("John", "Smith-123")


class TestEmployee(unittest.TestCase):
    """Test the Employee class."""

    def test_defaults(self):
        """Test required default values."""
        employee = Employee()
        self.assertEqual(employee.review_date, date(1900, 1, 1))
        self.assertEqual(employee.review_rating, 3)

    def test_valid_review_data(self):
        """Test valid review data."""
        employee = Employee("john", "smith", "2026-08-19", 5)
        self.assertEqual(employee.review_date, date(2026, 8, 19))
        self.assertEqual(employee.review_rating, 5)
        self.assertEqual(str(employee), "John,Smith,2026-08-19,5")

    def test_invalid_review_date(self):
        """Test invalid review date."""
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_date = "08/19/2026"

    def test_invalid_review_rating(self):
        """Test invalid review rating."""
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_rating = 6


if __name__ == "__main__":
    unittest.main()
