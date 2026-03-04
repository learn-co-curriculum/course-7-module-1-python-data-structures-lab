#this module contains operations related to sets

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Handles both Dictionary (Rubric) and Tuple (Test) formats.
    """
    majors = set()
    for s in student_list:
        # If it's a tuple, major is at index 2
        if isinstance(s, tuple):
            majors.add(s[2])

        else:
            majors.add(s["major"])
    return majors


def get_all_unique_courses(student_list):
    """
    Combines all courses from all students into one unique master set.
    Note: Test tuples don't have courses, so we skip them if they aren't there.
    """
    all_courses = set()
    for s in student_list:

        if isinstance(s, dict) and "courses" in s:
            all_courses.update(s["courses"])
    return all_courses