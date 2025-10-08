# This module contains functions to lazily generate student data.

def student_generator(students, major):

    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """

    return (s for s in students if s[2] == major)