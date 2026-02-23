# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # student[2] is the major field in the tuple (ID, Name, Major)
    # Curly braces {} with a comprehension create a set — duplicates are discarded automatically
    # e.g. if 3 students share "Mathematics", it still only appears once in the result
    return {student[2] for student in student_list}
