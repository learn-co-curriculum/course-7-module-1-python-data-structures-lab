# This module contains functions to process student data.
from student_data import students
def format_student_data(student):
    
    student_id, name, major = student
    message = f"ID: {student_id} | Name: {name} | Major: {major}"; 
    return message
    pass

def display_students(student_list):
    
    for student in student_list:
        formatted = format_student_data(student)
        print(formatted)

    
    pass
display_students(students)
