# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # get majors and put them in a set which automatically discards duplicates
    majors = {student[2] for student in student_list}
    return majors
