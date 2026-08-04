# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set containing each unique student major.

    Args:
        student_list (list): A list of student tuples.

    Returns:
        set: A set of unique majors found in the student list.
    """
    return {
        student[2]
        for student in student_list
    }