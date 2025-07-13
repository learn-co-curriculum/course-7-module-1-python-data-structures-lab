# This module contains functions for filtering student data.
from .data_processing import display_students
from .student_data import students

def filter_students_by_major(student_list, major):

    filtered = [student for student in student_list if student[2] == major]
    
    if filtered:
        return filtered
    else:
        return []

filter_students_by_major(students, "Computer Science")
