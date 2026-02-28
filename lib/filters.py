# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """Return a filtered list of students by major."""
    return [s for s in student_list if s[2].lower() == major.lower()]
