# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    filtered_results = []

    for student in student_list:

        current_major = student[2]

        if current_major == major:
            filtered_results.append(student)

    return filtered_results
