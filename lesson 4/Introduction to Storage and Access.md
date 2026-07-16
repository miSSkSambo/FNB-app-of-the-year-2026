# Unit 4: Introduction to Storage and Access

## 📖 Welcome to Unit 4

This unit introduces Python's core data structures for organizing and managing collections of information. You will learn how different data structures store, retrieve, and organize data efficiently for different programming tasks.

You will also explore:

- Mutable vs immutable data
- Processing structured data using iteration
- Representing real-world information using collections
- Building a foundation for working with datasets, APIs, and more advanced Python applications

---

# 🎯 Learning Objectives

By the end of this unit, you should be able to:

- Create and manipulate lists using:
  - Indexing
  - `append()`
  - `remove()`
  - `insert()`
  - Slicing
- Create and use dictionaries with key-value pairs
- Use dictionary methods:
  - `.get()`
  - `.keys()`
  - `.values()`
  - `.items()`
- Explain the difference between mutable and immutable data types
- Build a list of dictionaries to represent structured real-world data
- Iterate over lists and dictionaries using `for` loops

---

# 📦 Storage and Access

Python provides several built-in data structures to help organize and access information.

The four main structures covered in this unit are:

- Lists
- Dictionaries
- Lists of Dictionaries
- Tuples

---

# 📝 Lists

A **list** is an ordered, mutable collection of values stored in a single variable.

## Creating a List

```python
students = ["Amara", "Sipho", "Lerato"]
```

---

## Accessing Items

Lists use **index positions** starting from **0**.

```python
students[0]
```

**Output**

```python
'Amara'
```

Negative indexes count from the end.

```python
students[-1]
```

**Output**

```python
'Lerato'
```

---

## Common List Methods

### Add to the End

```python
students.append("John")
```

---

### Insert at a Position

```python
students.insert(1, "Nomsa")
```

---

### Remove by Value

```python
students.remove("Sipho")
```

---

### Remove by Index

```python
students.pop(0)
```

Returns the removed item.

---

### Count Items

```python
len(students)
```

---

## Example

```python
students = ["Amara", "Sipho", "Lerato"]

students.append("John")
students.insert(1, "Nomsa")
students.remove("Sipho")

print(students)
```

**Output**

```python
['Amara', 'Nomsa', 'Lerato', 'John']
```

---

# 📚 Dictionaries

A **dictionary** stores information as **key-value pairs**.

Think of it like a lookup table where every value has a name.

## Creating a Dictionary

```python
contact = {
    "name": "Amara",
    "phone": "071 234 5678"
}
```

---

## Access Values

```python
contact["name"]
```

**Output**

```python
'Amara'
```

---

## Safe Access with `.get()`

Using `.get()` prevents errors if the key does not exist.

```python
contact.get("email")
```

**Output**

```python
None
```

---

## Dictionary Methods

### Keys

```python
contact.keys()
```

Returns all keys.

---

### Values

```python
contact.values()
```

Returns all values.

---

### Items

```python
contact.items()
```

Returns key-value pairs.

---

## Example

```python
contact = {
    "name": "Amara",
    "phone": "071 234 5678"
}

print(contact.get("name"))
print(contact.keys())
print(contact.values())
```

---

# 🗂️ Lists of Dictionaries

One of Python's most useful data structures is a **list of dictionaries**.

Each dictionary represents one record.

The list stores multiple records together.

Example:

```python
students = [
    {
        "name": "Amara",
        "age": 20
    },
    {
        "name": "Sipho",
        "age": 22
    },
    {
        "name": "Lerato",
        "age": 21
    }
]
```

---

## Iterating Through Records

```python
for student in students:
    print(student["name"])
```

**Output**

```python
Amara
Sipho
Lerato
```

---

## Why is this Important?

Lists of dictionaries are commonly used for:

- Student records
- Contact lists
- Product inventories
- Employee databases
- JSON data from APIs
- Database query results

This structure forms the basis of many real-world Python applications.

---

# 🔒 Tuples

A **tuple** is similar to a list, but it is **immutable**.

This means it **cannot be changed after creation**.

---

## Creating a Tuple

```python
coordinates = (26.2, 28.0)
```

---

## Good Uses for Tuples

Use tuples for data that should never change.

Examples include:

- GPS coordinates
- RGB colour values
- Days of the week
- Mathematical constants

---

## Attempting to Modify a Tuple

```python
coordinates[0] = 25.8
```

Produces:

```python
TypeError
```

---

# 🔄 Mutable vs Immutable

| Mutable | Immutable |
|----------|-----------|
| Can be changed | Cannot be changed |
| List | Tuple |
| Dictionary | String |
| Set | Integer |
| | Float |

---

# 🔁 Iterating Through Collections

Python uses **for loops** to process collections.

## Loop Through a List

```python
students = ["Amara", "Sipho", "Lerato"]

for student in students:
    print(student)
```

---

## Loop Through a Dictionary

```python
contact = {
    "name": "Amara",
    "phone": "071 234 5678"
}

for key, value in contact.items():
    print(key, value)
```

---

# 💡 Summary

In this unit you learned:

- What lists are and how to manipulate them
- How dictionaries store key-value pairs
- How to safely retrieve dictionary values
- Why lists of dictionaries are widely used
- The difference between mutable and immutable data
- How tuples protect data from modification
- How to iterate through lists and dictionaries using `for` loops

These concepts provide the foundation for working with structured data, databases, APIs, and larger Python programs.

---

# 🚀 Key Takeaways

✅ Lists are ordered and mutable.

✅ Dictionaries store information as key-value pairs.

✅ Lists of dictionaries represent collections of records.

✅ Tuples are immutable and protect important data.

✅ `for` loops make processing collections simple and efficient.

Mastering these structures is an essential step toward becoming a proficient Python programmer.
