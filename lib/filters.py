# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    filtered_students = []
    for student in student_list:
        if student[2] == major:  # Assuming major is at index 2
            filtered_students.append(student)
    return filtered_students
