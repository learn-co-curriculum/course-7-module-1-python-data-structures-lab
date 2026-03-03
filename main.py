from lib.student_data import students
from lib.filters import filter_students_by_major
from lib.data_processing import display_students
from lib.set_operations import unique_majors
from lib.data_generator import student_generator


print("----- ALL STUDENTS -----")
display_students(students)


print("\n----- FILTERED: Computer Science -----")
cs_students = filter_students_by_major(students, "Computer Science")
display_students(cs_students)


print("\n----- UNIQUE MAJORS -----")
print(unique_majors(students))


print("\n----- GENERATOR TEST (Mathematics) -----")
gen = student_generator(students, "Mathematics")

for student in gen:
    print(student)