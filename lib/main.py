from student_data import students

from filters import filter_students_by_major

from data_processing import (
    format_student_data,
    display_students
)

from set_operations import unique_majors

from data_generator import student_generator


def main():

    print("\nALL STUDENTS")
    display_students(students)

    print("\nCOMPUTER SCIENCE STUDENTS")

    cs_students = filter_students_by_major(
        students,
        "Computer Science"
    )

    display_students(cs_students)

    print("\nUNIQUE MAJORS")

    print(unique_majors(students))

    print("\nGENERATOR EXAMPLE")

    cs_generator = student_generator(
        students,
        "Computer Science"
    )

    for student in cs_generator:
        print(format_student_data(student))


if __name__ == "__main__":
    main()