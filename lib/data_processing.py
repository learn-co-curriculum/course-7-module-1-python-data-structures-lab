# This module contains functions to process student data.

def format_student_data(student):
    """
    Given a student tuple (id, name, major), return:
    "ID: 101 | Name: Alice Johnson | Major: Computer Science"
    """
    sid, name, major = student
    return f"ID: {sid} | Name: {name} | Major: {major}"


def display_students(students):
    """
    Loop through all students and print each student's formatted details.
    """
    for s in students:
        print(format_student_data(s))