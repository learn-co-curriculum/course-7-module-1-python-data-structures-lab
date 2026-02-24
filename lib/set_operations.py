# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    majors_set = set()
    
    
    for student in student_list:
        
        major = student[2]
        
        majors_set.add(major)
        
    return majors_set
