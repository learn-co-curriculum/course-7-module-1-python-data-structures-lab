# Student Data Processing Project

This project demonstrates the use of essential Python data structures and techniques, including lists, tuples, sets, list comprehensions, set comprehensions, generator expressions, and modular program organization. It provides functions for generating, filtering, formatting, displaying, and analyzing student information in a clean and efficient way.

### Project Setup

- Download or clone the project repository onto your computer.
- Open the project folder in your development environment or terminal.
- Create and activate a virtual environment.
- Install any required testing tools, such as pytest, if your environment uses automated testing.
- Run the test suite to verify that all modules function as expected.

### Project Structure

The project is organized into several modules:

- data_generator.py – Contains functionality for lazily generating student records using generator expressions.
- data_processing.py – Provides functions for formatting student information and displaying multiple student records.
- filters.py – Includes functionality for filtering students by major using list comprehensions.
- set_operations.py – Contains tools for extracting unique student majors using set comprehensions.
- student_data.py – Stores the initial student records used throughout the project.
- testing folder – Contains additional student datasets and automated test files used to verify correctness.

Each module focuses on a specific part of the overall workflow to keep the program well-structured and easy to maintain.

### Features
- Student Generation
The project includes a generator-based filtering system designed for memory-efficient processing of student records. Rather than loading all matching records at once, this generator produces them one at a time, making it suitable for larger datasets.

- Student Formatting and Display
The project formats student data into a readable, descriptive sentence containing the student’s ID, name, and major. Another function displays any number of students by applying this formatting consistently.

- Filtering Students by Major
The project includes a filtering system that returns a new list containing only students whose major matches a specified subject. The filtering is case-insensitive and uses list comprehension to meet structural requirements of the assignment.

- Unique Major Extraction
The project is capable of identifying all unique majors represented in a dataset. This is done through set comprehension, ensuring that duplicate majors are automatically removed.

### Usage Summary

Users can:

- Display all student records in a clearly readable format.
- Filter students by major either as a list or as a lazy generator.
- Determine all unique majors represented in the dataset.
- Work with modular and well-organized code designed to scale and handle student data efficiently.

Testing

Automated tests confirm:
- Correct behavior of the generator function.
- Proper formatting and display of student information.
- Accurate filtering results.
- Correct extraction of unique majors, including handling of empty datasets.
- Proper use of required Python structures and comprehensions.
- Running the tests ensures that all required project criteria are met.