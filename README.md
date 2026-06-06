# Student Data Management System

## Overview

This project implements a Student Data Management System using Python data structures and comprehension techniques. The application demonstrates how to store, filter, process, and retrieve student records efficiently using lists, tuples, sets, list comprehensions, set comprehensions, and generator expressions.

## Learning Objectives

This project demonstrates:

* Using lists and tuples to store structured student data.
* Filtering records with list comprehensions.
* Formatting and displaying student information.
* Using set comprehensions to identify unique majors.
* Using generator expressions for memory-efficient data processing.
* Writing modular and maintainable Python code.

## Project Structure

```text
lib/
├── __init__.py
├── student_data.py
├── filters.py
├── data_processing.py
├── set_operations.py
└── data_generator.py
```

## Features

### Student Record Storage

Student records are stored as tuples containing:

```python
(student_id, student_name, major)
```

Example:

```python
(101, "Alice Johnson", "Computer Science")
```

### Filter Students by Major

The `filter_students_by_major()` function uses a list comprehension to return students enrolled in a specified major.

Example:

```python
filter_students_by_major(students, "Mathematics")
```

### Format Student Data

The `format_student_data()` function converts a student tuple into a readable string.

Example output:

```text
ID: 101 | Name: Alice Johnson | Major: Computer Science
```

### Display Student Records

The `display_students()` function loops through all students and prints formatted student information.

### Find Unique Majors

The `unique_majors()` function uses a set comprehension to return all unique majors represented in the student dataset.

Example output:

```python
{"Computer Science", "Mathematics", "Physics"}
```

### Student Generator

The `student_generator()` function uses a generator expression to lazily return students matching a specified major.

Example:

```python
math_students = student_generator(students, "Mathematics")

print(next(math_students))
```

This approach is memory efficient because records are generated only when needed.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd course-7-module-1-python-data-structures-lab
```

Install dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

## Running Tests

Run the test suite with:

```bash
pytest -x
```

Expected result:

```text
7 passed
```

## Technologies Used

* Python 3
* Lists
* Tuples
* Sets
* List Comprehensions
* Set Comprehensions
* Generator Expressions
* Pytest

## Author

Vincent
