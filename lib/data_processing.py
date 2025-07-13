# This module contains functions to process student data.

def format_student_data(student):
    return (f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}")
    # TODO: Implement this function

def display_students(student_list):
    """Display student records"""
    print("\nStudent Records:")
    for student in student_list:
        output = format_student_data(student=student)
        print(output)
