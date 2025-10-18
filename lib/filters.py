# This module contains functions for filtering student data.
from student_data import students



def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
   
    
    filter_list = [Name for (ID, Name, Major) in student_list if major == Major]
    
    print(filter_list)

    


filter_students_by_major(students, "Computer Science")
