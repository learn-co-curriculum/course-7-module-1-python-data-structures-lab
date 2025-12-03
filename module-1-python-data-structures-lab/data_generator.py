
# Generator function to iterate students by the specific major 

def student_generator(students, major):
    
    # Generator expression:
    return (student for student in students if student[2] == major)


# This block runs only if we execute this file directly.
if __name__ == "__main__":
    from student_data import students

    print("Mathematics students (using generator):")
    math_gen = student_generator(students, "Mathematics")

    # Iterate through the generator
    for student in math_gen:
        print(student)
