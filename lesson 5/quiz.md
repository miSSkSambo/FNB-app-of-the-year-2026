# Python Conditional Logic – Questions & Answers

## 1. The expression `if '@' in email:` checks whether `@` exists in the email string.

**Answer:** ✅ True

---

## 2. In an `if/elif/else` structure, Python evaluates every condition before deciding which block to execute.

**Answer:** ❌ False

**Explanation:** Python evaluates conditions from top to bottom and stops as soon as it finds the first condition that is `True`.

---

## 3. What is the difference between `elif` and a second `if`?

- No difference — they work the same way
- ✅ **`elif` is only checked if all previous conditions were False; a second `if` is always checked**
- `elif` can have an `else`; a second `if` cannot
- `elif` is faster than `if`

---

## 4. The `in` keyword can only be used with lists.

**Answer:** ❌ False

**Explanation:** The `in` keyword works with lists, strings, tuples, sets, dictionaries (checks keys), and other iterable objects.

---

## 5. A ticket booking system should approve a booking only if the customer is at least 18 years old or is accompanied by an adult. Which condition correctly represents this rule?

- `if age >= 18 and accompanied:`
- ✅ **`if age >= 18 or accompanied:`**
- `if not age >= 18 and accompanied:`
- `if age == 18 or not accompanied:`

---

## 6. The expression `if '@' in email:` checks whether `@` exists in the email string.

**Answer:** ✅ True

---

## 7. The `else` block is executed only when every preceding `if` and `elif` condition is False.

**Answer:** ✅ True

---

## 8. The `not` operator changes `True` to `False` and `False` to `True`.

**Answer:** ✅ True

---

## 9. What does `not True` evaluate to?

- `true`
- `none`
- ✅ **`false`**
- `0`

---

## 10. What does `if username:` check?

- Whether `username` equals `True`
- ✅ **Whether `username` is not empty, `None`, or `0`**
- Whether `username` is a string
- Whether `username` is defined

---

# Summary

| Question | Correct Answer |
|----------|----------------|
| 1 | True |
| 2 | False |
| 3 | `elif` is only checked if all previous conditions were False; a second `if` is always checked |
| 4 | False |
| 5 | `if age >= 18 or accompanied:` |
| 6 | True |
| 7 | True |
| 8 | True |
| 9 | `false` |
| 10 | Whether `username` is not empty, `None`, or `0` |

---

## Key Concepts Covered

- `if`, `elif`, and `else`
- Logical operators (`and`, `or`, `not`)
- Membership operator (`in`)
- Boolean values (`True` and `False`)
- Truthy and falsy values
- Conditional decision-making in Python
