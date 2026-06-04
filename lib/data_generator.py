# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    return (
        student
        for student in student_list
        if student[2].lower() == major.lower()
    )
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
   