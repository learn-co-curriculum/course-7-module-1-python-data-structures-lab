# This module contains operations related to sets.

def unique_majors(student_list):
    """Return a set of unique student majors using set comprehension."""
    return {s[2] for s in student_list}
