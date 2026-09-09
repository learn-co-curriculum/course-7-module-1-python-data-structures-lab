# This module contains functions to process student data.

def format_student_data(student):
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"

def display_students(student_list):
    for student in student_list:
        print(format_student_data(student))
 