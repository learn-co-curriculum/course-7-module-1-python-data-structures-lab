# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records that match the specified major.

    Args:
        student_list (list): A list of student tuples.
        major (str): The major used to filter students.

    Returns:
        generator: A generator that yields matching student
        records one at a time.
    """
    return (
        student
        for student in student_list
        if student[2].lower() == major.lower()
    )