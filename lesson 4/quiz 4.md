# 📚 Python Lists and Tuples – Questions & Answers

## Question 1
### Once a tuple has been created, individual values within it can be modified without creating a new tuple.

- True
- **False** ✅

**Explanation:**
Tuples are **immutable**, meaning their values cannot be changed after they are created. To make changes, you must create a new tuple.

---

## Question 2
### What does `.pop(0)` do?

- Removes the last item
- **Removes the first item and returns it** ✅
- Removes `'Sipho'`
- Returns the length of the list

**Explanation:**
The `.pop(index)` method removes and returns the element at the specified index. Since indexing starts at `0`, `.pop(0)` removes the first item.

```python
students = ["Sipho", "John", "Aisha"]
first = students.pop(0)

print(first)      # Sipho
print(students)   # ['John', 'Aisha']
```

---

## Question 3
### Which method removes `'Sipho'` by value?

- `.pop(1)`
- **`.remove('Sipho')`** ✅
- `.delete('Sipho')`
- `.discard('Sipho')`

**Explanation:**
The `.remove()` method removes the first occurrence of a specified value from a list.

```python
students = ["John", "Sipho", "Aisha"]
students.remove("Sipho")

print(students)
# ['John', 'Aisha']
```

---

## Question 4
### Why are lists considered mutable?

- They cannot be changed
- **They can be modified after creation** ✅
- They store key-value pairs
- They are immutable like tuples

**Explanation:**
Lists are mutable because you can add, remove, or modify their elements after they have been created.

---

## Question 5
### A list of dictionaries is a suitable way to store information about multiple students, where each student has attributes such as a name and student number.

- **True** ✅
- False

**Explanation:**
A list stores multiple records, while each dictionary stores information about one student.

```python
students = [
    {"name": "Amara", "student_number": "S001"},
    {"name": "Sipho", "student_number": "S002"},
    {"name": "Lerato", "student_number": "S003"}
]
```

---

## Question 6
### If `students = ['Amara', 'Sipho', 'Lerato']`, what is `len(students)`?

- 2
- **3** ✅
- 4
- 0

**Explanation:**
The list contains three items, so `len(students)` returns **3**.

```python
students = ['Amara', 'Sipho', 'Lerato']
print(len(students))
# 3
```

---

## Question 7
### Which method adds `'Thabo'` to the end of the list?

- `.insert('Thabo')`
- **`.append('Thabo')`** ✅
- `.add('Thabo')`
- `.push('Thabo')`

**Explanation:**
The `.append()` method adds a new element to the end of a list.

```python
students = ["Amara", "Sipho"]
students.append("Thabo")

print(students)
# ['Amara', 'Sipho', 'Thabo']
```

---

## Question 8
### Which method inserts `'Neo'` at index `1`?

- `.append('Neo')`
- **`.insert(1, 'Neo')`** ✅
- `.remove('Neo')`
- `.pop(1)`

**Explanation:**
The `.insert(index, value)` method inserts an item at the specified position.

```python
students = ["Amara", "Sipho"]
students.insert(1, "Neo")

print(students)
# ['Amara', 'Neo', 'Sipho']
```

---

## Question 9
### If data should never change, a tuple is generally a better choice than a list.

- **True** ✅
- False

**Explanation:**
Tuples are immutable, making them ideal for storing data that should remain constant.

---

## Question 10
### Which method adds an item to the **END** of a list?

- `.insert()`
- `.add()`
- **`.append()`** ✅
- `.push()`

**Explanation:**
The `.append()` method always adds an item to the end of a list.

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
# [1, 2, 3, 4]
```

---

## 🎯 Key Takeaways

- **Lists** are mutable (can be modified).
- **Tuples** are immutable (cannot be modified).
- Use **`.append()`** to add to the end of a list.
- Use **`.insert(index, value)`** to insert at a specific position.
- Use **`.remove(value)`** to remove an item by value.
- Use **`.pop(index)`** to remove and return an item by index.
- Use **`len()`** to determine the number of items in a list.
- A **list of dictionaries** is an excellent way to store multiple records with attributes.
