# 🐍 Python Unit 2 – String Manipulation and Formatting

## 📖 Overview

This unit introduces the essential techniques for working with **strings** (text) in Python. Strings are one of the most commonly used data types in programming, and learning how to manipulate them is an important skill for application development.

In this unit, you will learn how to:

- Transform text using built-in string methods
- Search and modify strings
- Count characters
- Access specific characters using indexing and slicing
- Format output using modern Python **f-strings**
- Combine strings together

By the end of this unit, you'll be able to process and display text effectively in your Python programs.

---

# 🎯 Learning Objectives

After completing this unit, you should be able to:

- ✅ Apply at least **7 string methods**
  - `upper()`
  - `lower()`
  - `title()`
  - `strip()`
  - `replace()`
  - `find()`
  - `split()`
- ✅ Use `len()` to count characters in a string
- ✅ Access individual characters using indexing
- ✅ Extract parts of strings using slicing
- ✅ Format output using **f-strings**
- ✅ Concatenate strings using the `+` operator

---

# 📚 Why Strings Matter

Strings are everywhere in software development.

Examples include:

- Usernames
- Passwords
- Search results
- Chat messages
- Button labels
- Error messages
- Email addresses
- Product names

Python provides powerful built-in tools that allow developers to transform, search, and display text efficiently.

---

# 🔧 String Methods

A **method** is a built-in function that belongs to an object.

Methods are called using **dot notation**.

```python
variable.method()
```

## 1. `upper()`

Converts all letters to uppercase.

```python
name = "Katlego"
print(name.upper())
```

**Output**

```
KATLEGO
```

---

## 2. `lower()`

Converts all letters to lowercase.

```python
name = "Kaltego"
print(name.lower())
```

**Output**

```
Katlego
```

---

## 3. `title()`

Capitalizes the first letter of every word.

```python
name = "jonathan tshena"
print(name.title())
```

**Output**

```
Katlego Sambo
```

---

## 4. `strip()`

Removes spaces before and after a string.

```python
text = "   Python   "
print(text.strip())
```

**Output**

```
Python
```

---

## 5. `replace()`

Replaces one piece of text with another.

```python
sentence = "I love Java"
print(sentence.replace("Java", "Python"))
```

**Output**

```
I love Python
```

---

## 6. `find()`

Returns the position of the first occurrence of a character or word.

```python
text = "Python Programming"
print(text.find("Program"))
```

**Output**

```
7
```

If the text isn't found:

```python
print(text.find("Java"))
```

**Output**

```
-1
```

---

## 7. `split()`

Splits a string into a list.

```python
fruits = "Apple,Banana,Orange"
print(fruits.split(","))
```

**Output**

```python
['Apple', 'Banana', 'Orange']
```

---

# 📏 Counting Characters

Use the built-in `len()` function.

```python
language = "Python"

print(len(language))
```

**Output**

```
6
```

---

# 🔢 Indexing

Each character in a string has an index.

```python
text = "Python"
```

| Index | Character |
|-------|-----------|
|0|P|
|1|y|
|2|t|
|3|h|
|4|o|
|5|n|

Examples:

```python
print(text[0])
```

Output

```
P
```

```python
print(text[1])
```

Output

```
y
```

Last character:

```python
print(text[-1])
```

Output

```
n
```

---

# ✂️ Slicing

Slicing extracts part of a string.

Syntax:

```python
string[start:end]
```

Example:

```python
text = "Python"

print(text[0:3])
```

Output

```
Pyt
```

Another example:

```python
print(text[2:6])
```

Output

```
thon
```

Using negative indexes:

```python
print(text[-3:])
```

Output

```
hon
```

---

# ✨ f-Strings

An **f-string** is the preferred way to insert variables into text.

Syntax:

```python
f"Text {variable}"
```

Example:

```python
name = "Katlego"

print(f"Welcome, {name}!")
```

Output

```
Welcome, Katlego!
```

Using methods inside an f-string:

```python
name = "Katlego"

print(f"Welcome, {name.title()}!")
```

Output

```
Welcome, Katlego!
```

Using expressions:

```python
age = 20

print(f"Next year you will be {age + 1}.")
```

Output

```
Next year you will be 21.
```

---

# ➕ String Concatenation

Strings can be joined using the `+` operator.

```python
first = "Sambo"
last = "Sambo"

full = first + " " + last

print(full)
```

Output

```
Katlego Sambo
```

Using an f-string is cleaner:

```python
print(f"{first} {last}")
```

Output

```
Katlego Sambo
```

---

# 📝 Summary

In this unit you learned how to:

- Convert text to uppercase, lowercase, and title case
- Remove unwanted spaces
- Replace words in a string
- Search for text
- Split strings into lists
- Count characters using `len()`
- Access characters using indexing
- Extract text using slicing
- Format output using f-strings
- Concatenate strings

These skills form the foundation for handling text in Python and are used in nearly every Python application.

---

# 🚀 Next Steps

Continue practicing by creating programs that:

- Format user names
- Validate passwords
- Process text input
- Build greeting applications
- Create simple text-based projects

Happy Coding! 🎉
