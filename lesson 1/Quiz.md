# 🐍 Python Fundamentals Quiz – Questions & Answers

This repository contains a Python Fundamentals quiz with the correct answers and explanations. It is intended as a study guide for beginners learning Python.

---

## Question 1

### Which combination correctly matches Python applications with the examples provided?

- ❌ Data Science – Instagram; Web Development – NASA
- ❌ Machine Learning – Pinterest; Automation – Spotify
- ✅ **Data Science – Netflix and Spotify; Web Development – Instagram and Pinterest**
- ❌ Mobile Development – Google and NASA

### Explanation
Python is widely used for:
- **Data Science:** Netflix and Spotify use Python for analytics and recommendations.
- **Web Development:** Instagram and Pinterest use Python (primarily Django) to power their web applications.

---

## Question 2

### If `age = 25`, then `type(age)` returns `int`.

- ✅ True
- ❌ False

### Explanation

```python
age = 25
print(type(age))
```

Output:

```python
<class 'int'>
```

The value `25` is an integer (`int`).

---

## Question 3

### Which file name would VS Code recognize as a Python script?

- ❌ program.txt
- ❌ program.docx
- ✅ **program.py**
- ❌ program.exe

### Explanation

Python source files always use the `.py` extension.

Example:

```python
hello.py
```

---

## Question 4

### A variable can store different types of values, such as text, numbers, and Boolean values.

- ✅ True
- ❌ False

### Explanation

Python variables can store many different data types.

Example:

```python
name = "Jonathan"
age = 33
height = 1.75
is_student = False
```

---

## Question 5

### A student writes the following code:

```python
name = "Thabo"
```

What does the variable **name** represent?

- ❌ A function that prints text
- ✅ **A named container storing a text value**
- ❌ A decimal number
- ❌ A Boolean value

### Explanation

`name` is a variable that stores the string `"Thabo"`.

---

## Question 6

### The `print()` function is used to display output in the terminal.

- ✅ True
- ❌ False

### Explanation

Example:

```python
print("Hello, World!")
```

Output:

```
Hello, World!
```

---

## Question 7

### If `name = "Amara"`, then `type(name)` returns `str`.

- ✅ True
- ❌ False

### Explanation

```python
name = "Amara"
print(type(name))
```

Output:

```python
<class 'str'>
```

Strings represent text in Python.

---

## Question 8

### What does the list itself represent in a list of dictionaries?

- ❌ A single record
- ✅ **All records**
- ❌ A tuple
- ❌ A key-value pair

### Explanation

Example:

```python
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 21}
]
```

- The **list** contains **all records**.
- Each **dictionary** represents one record.
- Each item inside a dictionary is a key-value pair.

---

## Question 9

### Why are lists of dictionaries powerful?

- ❌ They prevent iteration
- ✅ **They mimic database query results and API responses**
- ❌ They replace tuples
- ❌ They store immutable values

### Explanation

Lists of dictionaries are commonly used because they closely resemble:

- Database query results
- JSON data
- REST API responses

Example:

```python
employees = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
```

---

## Question 10

### Which command verifies that Python has been installed correctly in the terminal?

- ❌ python --check
- ❌ python version
- ✅ **python --version**
- ❌ check python

### Explanation

Run the following command:

```bash
python --version
```

Example output:

```text
Python 3.13.2
```

On some systems, you may use:

```bash
python3 --version
```

---


## 📚 Topics Covered

- Variables
- Data Types
- Strings
- Integers
- Booleans
- `type()` Function
- `print()` Function
- Python File Extensions
- Lists
- Dictionaries
- Lists of Dictionaries
- Terminal Commands

---

## 💻 Author: Katlego Sambo

Created as part of a Python Fundamentals learning journey.

Happy Coding! 🚀
