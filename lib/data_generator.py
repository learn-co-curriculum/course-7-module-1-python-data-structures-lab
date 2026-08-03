# This module contains functions to lazily generate student data.


def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    # returning student tuples where the student major (student[2]) matches the input keyword
    # using .lower() to make sure it is case insensitive
    return (student for student in student_list if student[2].lower() == major.lower())
