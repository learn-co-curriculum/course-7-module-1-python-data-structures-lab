
def unique_majors(students):
# Returns a set of unique majors from a list of students
    # Set comprehension:
    # go through each student and collect the major (index 2)
    majors = {student[2] for student in students}
    return majors


# This part is just for testing the function.
if __name__ == "__main__":
    from student_data import students  # reuse the same student list

    print("Unique majors:")
    print(unique_majors(students))
