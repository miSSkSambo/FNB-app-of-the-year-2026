# 🧠 Unit 5: Conditional Logic and Decision Making

## 📖 Introduction

**Unit 5: Conditional Logic and Decision Making**!

This unit introduces the principles of **decision-making in Python**, allowing your programs to respond differently based on specific conditions. You'll learn how logical comparisons control the flow of a program and how multiple conditions can be combined to create more flexible and intelligent outcomes.

You'll also discover how Python evaluates **membership** using the `in` keyword and how it interprets different values through **truthiness**. These concepts are essential for creating interactive programs that respond appropriately to user input and data.

---

# 🎯 Learning Objectives

By the end of this unit, you should be able to:

- ✅ Write `if`, `elif`, and `else` statements to control program flow.
- ✅ Use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) correctly.
- ✅ Combine conditions using logical operators (`and`, `or`, `not`).
- ✅ Use the `in` keyword to check membership in lists and strings.
- ✅ Create nested conditional statements where appropriate.
- ✅ Explain when to use `elif` instead of multiple separate `if` statements.

---

# 📚 Table of Contents

1. Selection of Tasks
2. Conditional Logic
3. Comparison Operators
4. Logical Operators
5. The `in` Keyword
6. Truthiness
7. Examples
8. Best Practices
9. Summary

---

# 1️⃣ Selection of Tasks

Programming often requires making decisions based on information provided by users or stored in variables.

Examples include:

- Is the user old enough to vote?
- Has the correct password been entered?
- Is a product in stock?
- Did the student pass the exam?

Python uses **conditional statements** to make these decisions.

---

# 2️⃣ Conditional Logic

Without conditional logic, every program would behave exactly the same way every time.

Conditional statements allow programs to execute different code depending on whether a condition is **True** or **False**.

Python evaluates conditions **from top to bottom** and executes the **first condition that is True**.

## Syntax

```python
if condition:
    # code

elif another_condition:
    # code

else:
    # code
```

### Example

```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

**Output**

```
You are an adult.
```

---

## Using `elif`

Use `elif` when checking multiple related conditions.

```python
score = 75

if score >= 80:
    print("Distinction")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

Output

```
Pass
```

---

## Why Indentation Matters

Python uses indentation instead of brackets.

Correct:

```python
if age >= 18:
    print("Adult")
```

Incorrect:

```python
if age >= 18:
print("Adult")
```

This will cause an **IndentationError**.

---

# 3️⃣ Comparison Operators

Comparison operators compare two values and return either **True** or **False**.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | True |
| `!=` | Not equal to | `5 != 3` | True |
| `>` | Greater than | `10 > 4` | True |
| `<` | Less than | `2 < 8` | True |
| `>=` | Greater than or equal to | `5 >= 5` | True |
| `<=` | Less than or equal to | `3 <= 6` | True |

---

## Assignment vs Comparison

One of the most common beginner mistakes is confusing `=` and `==`.

### Assignment

```python
age = 22
```

Stores the value **22** in the variable.

### Comparison

```python
age == 22
```

Checks whether `age` equals **22**.

---

# 4️⃣ Logical Operators

Logical operators allow multiple conditions to be combined.

## `and`

Both conditions must be **True**.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry granted")
```

Output

```
Entry granted
```

---

## `or`

At least one condition must be **True**.

```python
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today")
```

Output

```
No work today
```

---

## `not`

Reverses the result.

```python
logged_in = False

if not logged_in:
    print("Please log in.")
```

Output

```
Please log in.
```

---

## Combining Conditions

```python
temperature = 28
is_sunny = True

if temperature > 25 and is_sunny:
    print("Perfect weather!")
```

---

# 5️⃣ The `in` Keyword

The `in` keyword checks whether something exists inside a collection.

---

## Checking Lists

```python
roles = ["admin", "editor", "viewer"]

if "admin" in roles:
    print("Administrator access granted.")
```

Output

```
Administrator access granted.
```

---

## Checking Strings

```python
email = "user@example.com"

if "@" in email:
    print("Valid email format.")
```

Output

```
Valid email format.
```

---

# 6️⃣ Truthiness

Python automatically treats certain values as either **True** or **False**.

These values are considered **Falsy**:

- `0`
- `""` (empty string)
- `None`
- `[]` (empty list)
- `{}` (empty dictionary)
- `False`

Everything else is generally considered **Truthy**.

---

## Example

```python
username = "Jonathan"

if username:
    print("Username entered.")
```

Output

```
Username entered.
```

---

Empty string example

```python
username = ""

if username:
    print("Username entered.")
else:
    print("Please enter a username.")
```

Output

```
Please enter a username.
```

---

# 7️⃣ Complete Example

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You may drive.")
elif age >= 18:
    print("You need a driver's license.")
else:
    print("You are too young to drive.")
```

Output

```
You may drive.
```

---

# 8️⃣ Best Practices

✔ Use meaningful variable names.

```python
is_student = True
```

instead of

```python
x = True
```

---

✔ Use `elif` for related conditions.

Good:

```python
if mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
```

---

✔ Keep conditions simple.

Instead of writing very long conditions, break them into variables.

```python
is_adult = age >= 18

if is_adult:
    print("Access granted")
```

---

✔ Use indentation consistently.

Python depends on indentation to determine program structure.

---

# 📝 Summary

By completing this unit, you have learned how to:

- Use `if`, `elif`, and `else` to control program flow.
- Compare values using comparison operators.
- Combine multiple conditions using logical operators.
- Check membership using the `in` keyword.
- Understand truthy and falsy values.
- Write cleaner and more readable decision-making code.

---

# 🚀 Key Takeaways

- `if` executes when a condition is **True**.
- `elif` checks additional conditions.
- `else` runs when all previous conditions are **False**.
- `==` compares values, while `=` assigns values.
- `and` requires all conditions to be true.
- `or` requires at least one condition to be true.
- `not` reverses a condition.
- `in` checks membership.
- Empty values are considered **Falsy**.
- Proper indentation is essential in Python.
