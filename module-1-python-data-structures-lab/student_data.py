
# List of students stored as tuples (ID, Name, Major)
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

# prints this file to quickly check if it works
if __name__ == "__main__":
    # to see the data when we run this file directly
    print("List of students:")
    for student in students:
        print(student)
