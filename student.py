"""Student grade management system.

This module provides a Student class to manage grades and generate
summary reports according to the lab's functional requirements.
"""

LETTER_A_MIN = 90
LETTER_B_MIN = 80
LETTER_C_MIN = 70
LETTER_D_MIN = 60
HONOR_ROLL_MIN = 90
PASSING_GRADE = 60
MIN_GRADE = 0
MAX_GRADE = 100


class Student:
    """Represents a student with a name, ID, and a list of grades."""

    def __init__(self, student_id, name):
        """Initialize a student with an ID and a name.

        Args:
            student_id: The student's unique identifier (non-empty string).
            name: The student's full name (non-empty string).

        Raises:
            ValueError: If student_id or name is empty.
        """
        if not student_id or not str(student_id).strip():
            raise ValueError("Student ID cannot be empty.")
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.student_id = str(student_id).strip()
        self.name = name.strip()
        self.grades = []

    def add_grade(self, grade):
        """Add a numeric grade to the student's record.

        Args:
            grade: A numeric value between 0 and 100.

        Raises:
            TypeError: If grade is not numeric.
            ValueError: If grade is outside the 0-100 range.
        """
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise TypeError(
                f"Grade must be a number, got {type(grade).__name__}."
            )
        if grade < MIN_GRADE or grade > MAX_GRADE:
            raise ValueError(
                f"Grade must be between {MIN_GRADE} and {MAX_GRADE}."
            )
        self.grades.append(float(grade))

    def calculate_average(self):
        """Calculate and return the average of all grades.

        Returns:
            The average grade as a float, or 0.0 if there are no grades.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Return the letter grade corresponding to the average.

        Returns:
            A single character: 'A', 'B', 'C', 'D', or 'F'.
        """
        average = self.calculate_average()
        if average >= LETTER_A_MIN:
            return "A"
        if average >= LETTER_B_MIN:
            return "B"
        if average >= LETTER_C_MIN:
            return "C"
        if average >= LETTER_D_MIN:
            return "D"
        return "F"

    def is_passing(self):
        """Return True if the student's average is a passing grade."""
        return self.calculate_average() >= PASSING_GRADE

    def is_honor_roll(self):
        """Return True if the student qualifies for the Honor Roll."""
        return self.calculate_average() >= HONOR_ROLL_MIN

    def remove_grade_by_value(self, value):
        """Remove the first grade matching the given value.

        Args:
            value: The numeric grade value to remove.

        Returns:
            True if a grade was removed, False if the value was not found.
        """
        try:
            numeric_value = float(value)
        except (TypeError, ValueError):
            print(f"Error: '{value}' is not a valid numeric grade.")
            return False

        if numeric_value in self.grades:
            self.grades.remove(numeric_value)
            print(f"Grade {numeric_value} removed successfully.")
            return True

        print(f"Error: Grade {numeric_value} not found.")
        return False

    def remove_grade_by_index(self, index):
        """Remove a grade at the given index position.

        Args:
            index: The zero-based position of the grade to remove.

        Returns:
            True if a grade was removed, False otherwise.
        """
        try:
            position = int(index)
        except (TypeError, ValueError):
            print(f"Error: '{index}' is not a valid index.")
            return False

        if 0 <= position < len(self.grades):
            removed = self.grades.pop(position)
            print(f"Grade {removed} removed from index {position}.")
            return True

        print(
            f"Error: Index {position} is out of range. "
            f"Valid range: 0 to {len(self.grades) - 1}."
        )
        return False

    def generate_report(self):
        """Print a formatted summary report for the student."""
        status = "Passed" if self.is_passing() else "Failed"
        honor = "Yes" if self.is_honor_roll() else "No"
        separator = "=" * 40

        print(separator)
        print("       STUDENT SUMMARY REPORT")
        print(separator)
        print(f"Student ID     : {self.student_id}")
        print(f"Student Name   : {self.name}")
        print(f"Grades Count   : {len(self.grades)}")
        print(f"Average Grade  : {self.calculate_average():.2f}")
        print(f"Letter Grade   : {self.get_letter_grade()}")
        print(f"Status         : {status}")
        print(f"Honor Roll     : {honor}")
        print(separator)


def main():
    """Run a demonstration of the Student grade management system."""
    print("--- Student Grade Management System ---")

    try:
        student = Student("STU-001", "Alice Johnson")
    except ValueError as error:
        print(f"Failed to create student: {error}")
        return

    grades_to_add = [100, 95.5, 88, 92, 78]
    for grade in grades_to_add:
        try:
            student.add_grade(grade)
        except (TypeError, ValueError) as error:
            print(f"Could not add grade {grade}: {error}")

    print("\nTesting invalid inputs:")
    invalid_inputs = ["Fifty", -10, 150, None]
    for invalid in invalid_inputs:
        try:
            student.add_grade(invalid)
        except (TypeError, ValueError) as error:
            print(f"Could not add grade {invalid}: {error}")

    print("\nRemoving a grade by value (88):")
    student.remove_grade_by_value(88)

    print("\nRemoving a grade by index (0):")
    student.remove_grade_by_index(0)

    print("\nTrying to remove an out-of-range index (99):")
    student.remove_grade_by_index(99)

    print()
    student.generate_report()


if __name__ == "__main__":
    main()
