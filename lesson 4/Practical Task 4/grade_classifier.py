# grade_classifier.py

# Collect learner details
name = input("Enter learner's name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Assign grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Determine pass/fail status
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Check for intervention
intervention = []

if mark1 < 40:
    intervention.append("Subject 1")

if mark2 < 40:
    intervention.append("Subject 2")

if mark3 < 40:
    intervention.append("Subject 3")

# Display report card
print("\n==============================")
print("      STUDENT REPORT CARD")
print("==============================")

print(f"Learner Name : {name}")
print(f"Subject 1    : {mark1:.1f}")
print(f"Subject 2    : {mark2:.1f}")
print(f"Subject 3    : {mark3:.1f}")

print("------------------------------")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print(f"Status       : {status}")

if intervention:
    print("Intervention : Yes")
    print("Needs support in:", ", ".join(intervention))
else:
    print("Intervention : None")

print("==============================")
