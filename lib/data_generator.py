
def student_generator(student_list, major):
    
    return (
        student
        for student in student_list
        if student[2].lower() == major.lower()
    )