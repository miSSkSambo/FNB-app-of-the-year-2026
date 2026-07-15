# Unit 1: Introduction to Python, Strings and Numbers

## Overview
This unit introduces the fundamentals of Python programming and how it is used to solve real-world problems. It covers setting up a Python development environment, writing and running basic Python programs, and understanding how Python stores different types of data. These concepts form the foundation for all future programming skills.

---

## Learning Objectives
By the end of this unit, you should be able to:

- Explain what Python is and identify three real-world applications.
- Set up a Python development environment using Python and Visual Studio Code (VS Code).
- Write and execute a basic Python script using `print()` and `input()`.
- Create variables using the following data types:
  - `str` (String/Text)
  - `int` (Integer)
  - `float` (Decimal Number)
  - `bool` (Boolean: `True` or `False`)
- Use the `type()` function to determine the data type of a value.

---

## What is Python?

Python is a **high-level, interpreted programming language** released in **1991**. It is known for its simple, readable syntax, making it an excellent language for beginners while remaining powerful enough for professional software development.

### Common Applications
- 📊 Data Science (Netflix, Spotify)
- 🌐 Web Development (Instagram, Pinterest)
- 🤖 Automation
- 🧠 Machine Learning (Google, NASA)
- 📱 Mobile App Development (Kivy Framework)

---

## Development Environment

To start programming in Python, two main tools are required:

- **Python** – Executes your Python code.
- **Visual Studio Code (VS Code)** – The editor used to write and manage your code.

### Setup Steps
1. Install Python.
2. Install Visual Studio Code.
3. Install the **Microsoft Python Extension** in VS Code.
4. Create a project folder named **`app_academy`** to store all your course files.

The Python extension provides:
- Syntax highlighting
- Error detection
- One-click code execution

---

## Your First Python Script

A Python program is stored in a file with the **`.py`** extension.

Example:

```python
print("Hello, World!")
```

You can run the script by:
- Clicking the **Run/Play** button in VS Code.
- Running the following command in the terminal:

```bash
python hello.py
```

The `print()` function displays output to the terminal.

<img width="1237" height="957" alt="image" src="https://github.com/user-attachments/assets/46890acc-1c75-4db3-9ac1-927e2e22c04f" />

---

## Variables and Data Types

A **variable** stores a value and is created using the assignment operator (`=`).

Example:

```python
name = "Katlego"
```

### Basic Python Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| `str` | Text/String | `"Hello"` |
| `int` | Whole numbers | `25` |
| `float` | Decimal numbers | `3.14` |
| `bool` | True or False values | `True` |

Python automatically determines the data type, so you do not need to specify it.

Example:

```python
age = 21
height = 1.75
student = True
name = "Katlego"
```

---

## Checking Data Types

Use the `type()` function to identify the data type of a variable.

Example:

```python
name = "Kabelo"
age = 33

print(type(name))
print(type(age))
```

Output:

```text
<class 'str'>
<class 'int'>
```

---

## Key Takeaways

- Python is beginner-friendly yet widely used in industry.
- VS Code is used to write code, while Python executes it.
- Python files use the `.py` extension.
- The `print()` function displays output.
- Variables store data using the `=` operator.
- The four essential data types are:
  - `str`
  - `int`
  - `float`
  - `bool`
- The `type()` function shows the data type of a value.

---

## Summary

This unit introduced the fundamentals of Python programming, including setting up a development environment, writing your first Python program, creating variables, and working with the four primary data types. Understanding these concepts provides the foundation for building more advanced Python applications throughout the course.
