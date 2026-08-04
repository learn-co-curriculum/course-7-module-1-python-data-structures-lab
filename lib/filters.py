# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a list of students whose major matches the specified major.

    Args:
        student_list (list): A list of student tuples in the format
            (ID, Name, Major).
        major (str): The major to filter by.

    Returns:
        list: A list of student tuples whose major matches the
        specified major, ignoring case.
    """
    return [
        student
        for student in student_list
        if student[2].lower() == major.lower()
    ]