# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"

def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))

def student_to_dict(student):
    """
    Convert a single student tuple into a dictionary.
    Makes student data accessible by named keys instead of numeric indices.
    Example: (101, "Alice Johnson", "Computer Science")
    Returns: {"id": 101, "name": "Alice Johnson", "major": "Computer Science"}
    """
    # Map each tuple index to a meaningful key name
    return {
        "id": student[0],
        "name": student[1],
        "major": student[2]
    }


def students_to_dict(student_list):
    """
    Convert a list of student tuples into a dictionary keyed by student ID
    using a dictionary comprehension.
    Makes it easy to look up any student directly by their ID.
    Example: {101: {"name": "Alice Johnson", "major": "Computer Science"}, ...}
    """
    # Dictionary comprehension: key = student ID, value = dict of name and major
    # student[0] is the ID, used as the unique key for fast lookup
    return {
        student[0]: {"name": student[1], "major": student[2]}
        for student in student_list
    }