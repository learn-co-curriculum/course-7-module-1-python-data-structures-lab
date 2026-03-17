from student_data import students
from filter import filter_students_by_major
from data_processing import display_students
from set_operations import unique_majors
from data_generator import student_generator

# Filter
cs_students = filter_students_by_major(students, "Computer Science")
display_students(cs_students)

# Unique majors
print(unique_majors(students))

# Generator usage
gen = student_generator(students, "Mathematics")
print(next(gen))
print(next(gen))