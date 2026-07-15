# Arithmetic Operations and Type Casting

## Unit 3!

This unit introduces the mathematical operations that form the foundation of calculations in Python. You will learn how Python performs arithmetic, how numerical expressions are evaluated, and how to work with different data types when processing user input.

You will also explore **type casting**, which allows you to convert data between different types, and learn how to use Python's built-in number functions to manipulate and refine numeric values.

By the end of this unit, you will be able to build programs that perform accurate calculations and process numerical data effectively.

---

# Learning Objectives

By the end of this unit, you should be able to:

- Perform arithmetic using Python's seven arithmetic operators.
- Explain the difference between regular division (`/`) and floor division (`//`).
- Convert between data types using `int()`, `float()`, and `str()`.
- Apply the `round()` and `abs()` functions to numeric values.
- Build a multi-function calculator using arithmetic operations and type casting.

---

# Manipulating Numbers

Numbers are one of the most common data types used in programming. Python provides several arithmetic operators that allow you to perform mathematical calculations quickly and accurately.

---

# Arithmetic Operators

Python supports **seven arithmetic operators**.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 2` | `5.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 10` | `1024` |

---

## Example

```python
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 2)
print(10 // 3)
print(10 % 3)
print(2 ** 10)
```

### Output

```
15
5
50
5.0
3
1
1024
```

---

# Division vs Floor Division

Python has two different division operators.

## Regular Division (`/`)

Always returns a **float**, even if the answer is a whole number.

```python
print(10 / 2)
```

Output

```
5.0
```

---

## Floor Division (`//`)

Returns only the whole number by removing the decimal part.

```python
print(10 // 3)
```

Output

```
3
```

---

# The Type Casting Gotcha

One of the most common beginner mistakes involves the `input()` function.

The `input()` function **always returns a string**, even if the user enters numbers.

For example:

```python
num = input("Enter a number: ")
print(num + 5)
```

This produces a **TypeError** because Python cannot add a string and an integer.

---

# Correct Way Using Type Casting

Use `int()` for whole numbers.

```python
num = int(input("Enter a number: "))
print(num + 5)
```

Output (if the user enters `10`)

```
15
```

---

Use `float()` for decimal numbers.

```python
price = float(input("Enter a price: "))
print(price * 2)
```

---

# Type Casting Functions

Python provides three main type casting functions.

| Function | Converts To | Example |
|----------|-------------|---------|
| `int()` | Integer | `int("25")` |
| `float()` | Decimal | `float("25.5")` |
| `str()` | String | `str(25)` |

---

## Example

```python
age = int("21")
height = float("1.75")
student = str(12345)

print(age)
print(height)
print(student)
```

---

# Useful Number Functions

Python includes several built-in functions for working with numbers.

## round()

Rounds a number to a specified number of decimal places.

```python
print(round(3.14159, 2))
```

Output

```
3.14
```

---

## abs()

Returns the absolute (positive) value of a number.

```python
print(abs(-7))
```

Output

```
7
```

---

# Operator Precedence (BEDMAS)

Python follows the standard mathematical order of operations.

1. **B** – Brackets `()`
2. **E** – Exponents `**`
3. **DM** – Division `/`, Floor Division `//`, Modulus `%`, Multiplication `*`
4. **AS** – Addition `+`, Subtraction `-`

Remember the acronym:

> **BEDMAS**

---

## Example 1

```python
print((2 + 3) * 4)
```

Output

```
20
```

---

## Example 2

```python
print(2 + 3 * 4)
```

Output

```
14
```

Multiplication happens before addition because of **BEDMAS**.

---

# Unit Summary

After completing this unit, you should understand how to:

- ✅ Perform arithmetic calculations using Python's seven operators.
- ✅ Differentiate between division (`/`) and floor division (`//`).
- ✅ Convert data types using `int()`, `float()`, and `str()`.
- ✅ Use `round()` and `abs()` for working with numeric values.
- ✅ Apply BEDMAS to evaluate mathematical expressions correctly.
- ✅ Build calculator programs that process user input accurately.
