# This module contains functions to process student data.

def format_student_data(student):
    """
    Format a student's information into a readable string.

    Args:
        student (tuple): A student record in the format
            (ID, Name, Major).

    Returns:
        str: A formatted string containing the student's ID,
        name, and major.
    """
    return (f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}")


def display_students(student_list):
    """
    Display all students in the provided student list.

    Args:
        student_list (list): A list of student tuples.

    Returns:
        None
    """
    for student in student_list:
        print(format_student_data(student))