# This module contains functions to process student data.
from student_data import students
def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    student_id, name, major = student
    message = f"ID: {student_id} | Name: {name} | Major: {major}"; 
    return message
    pass

def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        formatted = format_student_data(student)
        print(formatted)

    
    


    pass
display_students(students)
