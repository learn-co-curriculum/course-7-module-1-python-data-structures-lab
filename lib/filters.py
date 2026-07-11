# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    """

    return [
        student
        for student in student_list
        if student[2].lower() == major.lower()
    ]
