#This module processes the student data

def format_student_data(student):
    """
    Format student data for display.
    This version is 'bilingual'—it works for both Dictionaries and Tuples.
    """
    # check if 'student' is in a Tuple
    if isinstance(student, tuple):
        student_id = student[0]
        name = student[1]
        major = student[2]
    
    # otherwise, treat it as a Dictionary 
    else:
        student_id = student["id"][0]
        name = student["id"][1]
        major = student["major"]
    
    return f"ID: {student_id} | Name: {name} | Major: {major}"

def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))

def calculate_average_gpa(student_list):
    """
    Calculates the average GPA using a generator expression () for memory efficiency.
    """
    if not student_list:
        return 0.0
        
    # The generator expression for lazy evaluation
    gpa_generator = (s["gpa"] for s in student_list)
    
    return sum(gpa_generator) / len(student_list)