from lib.student_data import students
from lib.filters import filter_students_by_major, get_high_gpa_students
from lib.set_operations import unique_majors, get_all_unique_courses
from lib.data_processing import display_students, calculate_average_gpa
from lib.data_generator import student_generator

def main():
    print("--- Student Management System ---")
    
    print("\nAll Students:")
    display_students(students)
    
    #show Unique Attributes in the sets
    print("\nUnique Majors:")
    print(unique_majors(students))
    
    print("\nAll Unique Courses:")
    print(get_all_unique_courses(students))
    
    #generator expression for gpa
    avg_gpa = calculate_average_gpa(students)
    print(f"\nAverage GPA of all students: {avg_gpa:.2f}")
    
    #Filters by Major 
    cs_students = filter_students_by_major(students, "Computer Science")
    print("\nFiltered (Computer Science):")
    display_students(cs_students)
    
    #The lazy Generator 
    print("\nLazy Generator Filter (Mathematics):")
    math_gen = student_generator(students, "Mathematics")
    for student in math_gen:
        # Accesses the Name from the ID tuple: (102, "Bob Smith")
        print(f"Lazy Result: {student['id'][1]}")

if __name__ == "__main__":
    main()