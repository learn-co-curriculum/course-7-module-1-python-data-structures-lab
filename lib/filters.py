# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    # student[2] is the major field in the tuple (ID, Name, Major)
    # .lower() on both sides ensures case-insensitive matching
    # e.g. "computer science" and "Computer Science" both match
    return [student for student in student_list if student[2].lower() == major.lower()]
