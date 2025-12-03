#simple dictionary functionality to the student Data and Management System

from student_data import students

def build_student_dictionary():
  #Returns a dictionary ß
    # dictionary comprehension
    student_dict = {student[0]: student[1] for student in students}
    return student_dict


# Only runs when this file is executed directly
if __name__ == "__main__":
    lookup = build_student_dictionary()
    print("Student Dictionary:")
    print(lookup)
