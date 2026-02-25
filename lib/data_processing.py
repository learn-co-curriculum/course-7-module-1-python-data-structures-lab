
def format_student_data(student):
    
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(student_list):
    
    for student in student_list:
        print(format_student_data(student))