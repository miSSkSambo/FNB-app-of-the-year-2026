# Unit 6 Quiz – Questions & Answers

## Question 1
**Both `break` and `continue` can be used only with `for` loops.**

- [ ] True
- [x] False ✅

**Explanation:**  
`break` and `continue` work with both **`for`** and **`while`** loops.

---

## Question 2
**What does `range(2, 10, 3)` generate?**

- [x] 2, 5, 8 ✅
- [ ] 2, 3, 4, 5, 6, 7, 8, 9
- [ ] 2, 5, 8, 11
- [ ] 3, 6, 9

**Explanation:**  
`range(start, stop, step)` starts at **2**, increments by **3**, and stops before **10**.

---

## Question 3
**The `continue` statement allows a loop to skip items that fail a condition without terminating the entire loop.**

- [x] True ✅
- [ ] False

**Explanation:**  
`continue` skips the current iteration and proceeds to the next iteration.

---

## Question 4
**What is the output of the following code?**

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

- [ ] 1 2 3 4 5
- [x] 1 2 4 5 ✅
- [ ] 1 2
- [ ] 3

**Explanation:**  
When `i == 3`, `continue` skips the `print()` statement.

---

## Question 5
**What does the `continue` statement do?**

- [ ] Exits the loop immediately
- [x] Skips to the next iteration without finishing the current one ✅
- [ ] Starts the loop over from the beginning
- [ ] Pauses execution

**Explanation:**  
`continue` skips the remaining statements in the current iteration.

---

## Question 6
**`range()` is memory-efficient because it generates numbers only when they are needed.**

- [x] True ✅
- [ ] False

**Explanation:**  
`range()` does not store all numbers in memory at once.

---

## Question 7
**The `break` statement skips the current iteration and continues with the next one.**

- [ ] True
- [x] False ✅

**Explanation:**  
`break` exits the loop immediately. `continue` skips the current iteration.

---

## Question 8
**A `while` loop is most appropriate when the exact number of iterations is known before the loop begins.**

- [ ] True
- [x] False ✅

**Explanation:**  
A `while` loop is best when the number of iterations is **unknown** beforehand.

---

## Question 9
**What is the output of the following code?**

```python
for i in range(3):
    print(i)
```

- [ ] 1 2 3
- [ ] 0 1 2 3
- [x] 0 1 2 ✅
- [ ] 1 2

**Explanation:**  
`range(3)` generates **0, 1, 2**.

---

## Question 10
**A `for` loop repeats a block of code once for every item in a sequence.**

- [x] True ✅
- [ ] False

**Explanation:**  
A `for` loop iterates through each item in a sequence such as a list, tuple, string, or `range`.

---

# Final Score

**Total Questions:** 10  
**Correct Answers:** 10/10 ✅
