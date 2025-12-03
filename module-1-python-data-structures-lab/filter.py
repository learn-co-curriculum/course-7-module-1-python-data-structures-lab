

def filter_students_by_major(students, major):
    #Returns a list of students who have the given major
    
    # List comprehension: go through each student and only keep the ones
    # where the major (index 2 in the tuple) matches the given major
    filtered_students = [student for student in students if student[2] == major]
    
    return filtered_students


# This part only runs if we execute this file directly.
# for testing the function.
if __name__ == "__main__":
    from student_data import students  # import the students list from student_data.py

    # Example: filter for Computer Science students
    cs_students = filter_students_by_major(students, "Computer Science")
    
    print("Students with major 'Computer Science':")
    for s in cs_students:
        print(s)
