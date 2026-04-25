# This module contains operations related to sets.

def unique_majors(students):
    return {student[2] for student in students}
