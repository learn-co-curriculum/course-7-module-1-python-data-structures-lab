#this module contains the generator

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency.
    Handles both Dictionary (Rubric) and Tuple (Test) formats.
    """
    for student in student_list:
        # first ,determine the student's major based on data type
        if isinstance(student, tuple):
            current_major = student[2]
        else:
            current_major = student["major"]

        # Check if the major matches => (case-insensitive)
        if current_major.lower() == major.lower():
            yield student