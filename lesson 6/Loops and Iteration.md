# 🔁 Loops and Iteration in Python

> **Unit 6 - Python Programming**
>
> Learn how to automate repetitive tasks using loops, making your programs cleaner, faster, and more efficient.

---

# 📚 Introduction

 **Unit 6!**

One of the greatest strengths of programming is automation. Instead of writing the same code repeatedly, Python allows you to use **loops** to perform repetitive tasks efficiently.

In this unit, you will learn how to:

- Repeat code using `for` and `while` loops.
- Work with lists, dictionaries, strings, and ranges.
- Control loop execution using `break` and `continue`.
- Combine loops with conditions to solve more complex problems.

By mastering loops, you'll be able to write cleaner, more efficient, and scalable Python programs.

---

# 🎯 Learning Objectives

By the end of this unit you should be able to:

- ✅ Write `for` loops to iterate over lists, dictionaries, strings, and `range()`.
- ✅ Write `while` loops that repeat until a condition becomes `False`.
- ✅ Use `range()` with start, stop, and step values.
- ✅ Use `break` to exit loops early.
- ✅ Use `continue` to skip the current iteration.
- ✅ Combine loops with conditions to solve real-world programming problems.

---

# 🔄 Why Use Loops?

Imagine needing to print 100 names.

Without loops:

```python
print("Student 1")
print("Student 2")
print("Student 3")
...
print("Student 100")
```

With a loop:

```python
for i in range(1, 101):
    print(f"Student {i}")
```

Much shorter, easier to read, and easier to maintain.

---

# 🔹 The `for` Loop

A **for loop** repeats a block of code for every item in a sequence.

### Basic Syntax

```python
for item in sequence:
    # code to repeat
```

---

## Example 1 – Loop Through a List

```python
students = ["Katlego", "Lerato", "Jonathan"]

for student in students:
    print(student)
```

**Output**

```
Katlego
Lerato
Jonathan
```

---

## Example 2 – Loop Through a String

```python
name = "Python"

for letter in name:
    print(letter)
```

**Output**

```
P
y
t
h
o
n
```

---

## Example 3 – Loop Through a Dictionary

```python
student = {
    "Name": "Katlego Sambo",
    "Age": 22,
    "Course": "Python"
}

for key, value in student.items():
    print(key, ":", value)
```

**Output**

```
Name : Katlego Sambo
Age : 22
Course : Python
```

---

# 📏 Using `range()`

The `range()` function generates a sequence of numbers.

It is commonly used with `for` loops.

---

## Example 1

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```


---

## Example 2

```python
for i in range(1, 11):
    print(i)
```

Output

```
1
2
3
4
5
6
7
8
9
10
```


---

## Example 3 – Step Value

```python
for i in range(0, 20, 2):
    print(i)
```

Output

```
0
2
4
6
8
10
12
14
16
18
```


---

## Example 4 – Countdown

```python
for i in range(10, 0, -1):
    print(i)
```

Output

```
10
9
8
7
6
5
4
3
2
1
```


---

## Understanding `range()`

| Function | Result |
|----------|---------|
| `range(5)` | 0 → 4 |
| `range(1,11)` | 1 → 10 |
| `range(0,20,2)` | Even numbers |
| `range(10,0,-1)` | Countdown |

---

### Why is `range()` Efficient?

Unlike a list, `range()` **does not store every number in memory**.

Instead, it generates each number only when needed.

This makes it memory-efficient even for very large loops.

---

# 🔁 The `while` Loop

A **while loop** continues running while its condition remains `True`.

### Basic Syntax

```python
while condition:
    # repeated code
```

---

## Example 1

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```


---

## Example 2 – User Input

```python
command = ""

while command != "quit":
    command = input("Enter command: ")

print("Program ended.")
```

The loop continues until the user types:

```
quit
```



---

## Infinite Loops

If you forget to update the variable inside a `while` loop, it never ends.

Incorrect:

```python
count = 1

while count <= 5:
    print(count)
```

This keeps printing:

```
1
1
1
1
1
...
```

Stop an infinite loop by pressing:

```
Ctrl + C
```

---

# ⛔ `break` and `continue`

Python gives us two useful keywords for controlling loops.

---

## `break`

Stops the loop immediately.

```python
for number in range(10):

    if number == 5:
        break

    print(number)
```

Output

```
0
1
2
3
4
```

The loop ends when it reaches **5**.

---

## `continue`

Skips the current iteration.

```python
for number in range(6):

    if number == 3:
        continue

    print(number)
```

Output

```
0
1
2
4
5
```

The number **3** is skipped.

---

## Difference

| `break` | `continue` |
|----------|------------|
| Ends the loop | Skips one iteration |
| Loop stops completely | Loop keeps running |

---

# 🔀 Combining Loops with Conditions

Loops become much more powerful when combined with `if` statements.

Example:

```python
numbers = [10, 15, 22, 31, 40]

for number in numbers:

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
```

Output

```
10 is even
15 is odd
22 is even
31 is odd
40 is even
```

---

# 🌍 Real-World Example

Suppose a teacher wants to calculate the total marks for students.

```python
marks = [75, 80, 92, 68, 88]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Total:", total)
print("Average:", average)
```

Output

```
Total: 403
Average: 80.6
```

---

# ⚠️ Common Mistakes

### Forgetting indentation

Incorrect

```python
for i in range(5):
print(i)
```

Correct

```python
for i in range(5):
    print(i)
```

---

### Infinite `while` loop

Incorrect

```python
count = 1

while count <= 5:
    print(count)
```

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

### Confusing `break` and `continue`

Remember:

- `break` ends the loop.
- `continue` skips one iteration.

---

# ✅ Best Practices

- Use `for` loops when you know the number of iterations.
- Use `while` loops when the number of repetitions is unknown.
- Always update variables inside `while` loops.
- Keep loop bodies simple and readable.
- Use meaningful variable names.
- Avoid unnecessary nested loops when possible.

---

# 💻 Practice Exercises

## Exercise 1

Print numbers from **1 to 20**.

<img width="825" height="953" alt="image" src="https://github.com/user-attachments/assets/a92cbac7-6418-45ec-b8e4-db04f32bb57d" />

---

## Exercise 2

Print every letter in your surname.

<img width="991" height="946" alt="image" src="https://github.com/user-attachments/assets/85d7d0eb-f2be-4486-9d4a-743b5b5d48d4" />

---

## Exercise 3

Print all even numbers between **2 and 50**.

<img width="966" height="951" alt="image" src="https://github.com/user-attachments/assets/7a512717-f12f-4b92-9527-e964ebcdc3e4" />

---

## Exercise 4

Ask the user to keep entering numbers until they enter **0**.

<img width="1057" height="803" alt="image" src="https://github.com/user-attachments/assets/e9025d8b-da4e-4ba4-9aeb-f7a555ac1d6f" />

---

## Exercise 5

Create a list of marks and print only the marks greater than **70**.

---

## Exercise 6

Count down from **20 to 1**.

---

# 📝 Key Takeaways

✔️ Loops eliminate repetitive code.

✔️ `for` loops iterate through sequences.

✔️ `range()` creates number sequences efficiently.

✔️ `while` loops repeat while a condition is `True`.

✔️ `break` exits a loop immediately.

✔️ `continue` skips the current iteration.

✔️ Combining loops with conditions enables powerful problem-solving.

---

# 🚀 Next Step

Once you're comfortable with loops, you'll be ready to tackle more advanced Python concepts such as functions, file handling, and object-oriented programming, where loops play a crucial role in building real-world applications.

Happy Coding! 🐍
