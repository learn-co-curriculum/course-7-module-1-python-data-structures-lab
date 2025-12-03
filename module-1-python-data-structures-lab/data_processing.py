
# Functions for displaying student data


def format_student_data(student):

    #Takes a single student tuple and returns a formatted string.
    
    # student[0] = ID, student[1] = Name, student[2] = Major
    formatted = f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"
    return formatted


def display_students(students):
    #Loops through a list of student tuples and prints each one
    
    # Go through each student in the list
    for student in students:
        # Print the formatted version of the student
        print(format_student_data(student))


# This part runs only if we execute this file directly.
if __name__ == "__main__":
    from student_data import students  # import the list from student_data.py

    print("All students:")
    display_students(students)
