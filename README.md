Data Structures Lab - Student Management System
I built this project to handle student data using different Python structures like lists, dictionaries, and sets. The main goal was to practice filtering data efficiently and using generators to keep things fast.

What’s in this project:
Student Data: I stored student info in dictionaries within a list. I used tuples for the student IDs since those shouldn't change.

Finding Majors & Courses: Used sets to pull out unique majors and combined all the different course sets into one master list of unique courses.

Filtering: Used list comprehensions to filter students by their major (case-insensitive) and by their GPA.

Memory Efficiency: I used a generator function with yield for "lazy" filtering and a generator expression to calculate the average GPA.

Files:
main.py - This is where you run the code to see the output.

lib/ - This folder has all the logic (filters, set operations, data, etc.).

testing/ - The test files to make sure the functions don't break.

How to run and use the program:

First, install the environment:
pipenv install

Get into the shell:
pipenv shell

Run the tests:
python -m pytest testing/test_filters.py

Then run the main script:
python main.py

Run the tests:
python -m pytest testing/test_filters.py

Notes:
I added some isinstance checks in the filters so the code works with both the dictionaries in my app and the tuples required.