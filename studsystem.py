
# Each student record will be stored as a tuple:
# (student_id, name, age, major, completed_courses)

# completed_courses will be a set

# List to store all students
students = []

# Function to add a student
def add_student(student_id, name, age, major, completed_courses):
    student = (
        student_id,
        name,
        age,
        major,
        set(completed_courses)  # convert courses to set
    )
    students.append(student)
    print(f"Student {name} added successfully.")


# Function to display all students
def display_students(student_list):
    print("\nStudent Records:")
    for student in student_list:
        student_id, name, age, major, courses = student
        print(f"ID: {student_id}, Name: {name}, Age: {age}, Major: {major}, Courses: {courses}")


# Filter students by major(list comprehension)
def filter_by_major(major):
    filtered = [student for student in students if student[3].lower() == major.lower()]
    return filtered


# Filter students by age greater than a value
def filter_by_age(min_age):
    filtered = [student for student in students if student[2] >= min_age]
    return filtered


# Set comprehension to track unique majors
def get_unique_majors():
    majors = {student[3] for student in students}
    return majors


# Track unique completed courses using set comprehension
def get_all_completed_courses():
    courses = {course for student in students for course in student[4]}
    return courses

# Generator expression 
def student_generator():
    return (student for student in students)


# Generator to filter students dynamically
def generator_filter_by_course(course_name):
    return (
        student for student in students
        if course_name.lower() in (course.lower() for course in student[4])
    )


# Add students example usage
add_student("S001", "Alice", 20, "Computer Science", ["Math", "Python", "Data Structures"])
add_student("S002", "Bob", 22, "Engineering", ["Physics", "Math"])
add_student("S003", "Charlie", 21, "Computer Science", ["Python", "AI"])
add_student("S004", "Diana", 23, "Mathematics", ["Statistics", "Algebra"])


# Display all students
display_students(students)


# Filter students by major
cs_students = filter_by_major("Computer Science")
display_students(cs_students)


# Filter students by age
older_students = filter_by_age(21)
display_students(older_students)


# Get unique majors
print("\nUnique Majors:")
print(get_unique_majors())


# Get all completed courses
print("\nAll Completed Courses:")
print(get_all_completed_courses())


# Use generator to process students
print("\nProcessing students using generator:")
gen = student_generator()

print(next(gen))
print(next(gen))


# Generator filtering example
print("\nStudents who completed Python:")
python_students = generator_filter_by_course("Python")

for student in python_students:
    print(student)