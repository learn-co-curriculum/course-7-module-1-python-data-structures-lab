# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    Unlike a list comprehension [], a generator expression () does not load
    all results into memory at once — it yields one record at a time on demand.
    This makes it ideal for processing large datasets efficiently.
    """
    # Parentheses () make this a generator expression instead of a list
    # Nothing is computed until next() is called on the result
    # student[2] is the major field in the tuple (ID, Name, Major)
    # Uses exact case matching — callers should pass the major exactly as stored
    return (student for student in student_list if student[2] == major)
