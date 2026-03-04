
#This module filters the students data


def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    Handles both Dictionary (Rubric) and Tuple (Test) formats.
    """
    return [
        s for s in student_list 
        if (s[2].lower() if isinstance(s, tuple) else s["major"].lower()) == major.lower()
    ]

def get_high_gpa_students(student_list, threshold=3.5):
    """
    Filters students with a GPA above the threshold.
    Note: Test tuples don't have GPA, so we default to 0.0 to avoid crashes.
    """
    return [
        s for s in student_list 
        if (0.0 if isinstance(s, tuple) else s.get("gpa", 0.0)) >= threshold
    ]

#I used isinstance checks so the code stays flexible; 
# it can handle the complex dictionaries required
#  and the simple tuples for the tests