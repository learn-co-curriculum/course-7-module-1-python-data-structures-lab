# Student Data Management System

## Overview

A Python project for storing, filtering, and processing student records using lists, tuples, sets, comprehensions, and generator expressions.

The system manages student information, filters records by major, displays formatted student data, tracks unique majors, and processes student records efficiently.

## Features

* Stores student records as tuples inside a list.
* Filters students by major using list comprehensions.
* Formats and displays student information.
* Tracks unique majors using set comprehensions.
* Uses generator expressions for efficient data processing.

## Functions

### `filter_students_by_major(student_list, major)`

Filters student records by major and returns a list containing only matching students.

### `format_student_data(student)`

Formats a student tuple into a readable string containing the student's ID, name, and major.

Example output:

```
ID: 101 | Name: Alice Johnson | Major: Computer Science
```

### `display_students(student_list)`

Loops through student records and displays each student's formatted information.

### `unique_majors(student_list)`

Returns a set containing all unique majors found in the student records.

### `student_generator(student_list, major)`

Returns a generator expression that yields students matching a given major without creating a separate list in memory.

## Data Structure Examples

Student records are stored as tuples:

```python
(101, "Alice Johnson", "Computer Science")
```

The collection of students is stored as a list:

```python
[
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics")
]
```

## Setup

Clone the repository:

```bash
git clone <repo-url>
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
