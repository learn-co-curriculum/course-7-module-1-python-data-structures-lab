# This module contains operations related to sets.
from student_data import students
def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """

    unique_majors = { major for ID,Name, major in student_list }
    return unique_majors


    pass



