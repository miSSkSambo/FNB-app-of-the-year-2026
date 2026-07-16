

# ==========================================
# Grade Report Generator
# ==========================================

# List of at least 5 students
students = [
    {"name": "Alice", "maths": 85, "english": 78, "science": 92},
    {"name": "Brian", "maths": 65, "english": 70, "science": 68},
    {"name": "Cindy", "maths": 48, "english": 55, "science": 50},
    {"name": "David", "maths": 90, "english": 88, "science": 95},
    {"name": "Emma", "maths": 35, "english": 42, "science": 40}
]

results = []
total_average = 0
highest_mark = 0
lowest_mark = 100

# Process each student
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3

    # Grade Logic
    if average >= 75:
        grade = "A"
        status = "Excellent"
    elif average >= 60:
        grade = "B"
        status = "Pass"
    elif average >= 50:
        grade = "C"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

    # Store results
    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

    total_average += average

    if average > highest_mark:
        highest_mark = average

    if average < lowest_mark:
        lowest_mark = average

# Class statistics
class_average = total_average / len(results)

# ==========================
# Display Report
# ==========================

print("=" * 60)
print("           CLASS GRADE REPORT")
print("=" * 60)

print(f"{'Name':<15}{'Average':<12}{'Grade':<10}{'Status'}")
print("-" * 60)

for student in results:
    print(f"{student['name']:<15}{student['average']:<12.2f}{student['grade']:<10}{student['status']}")

print("-" * 60)
print(f"Class Average : {class_average:.2f}")
print(f"Highest Mark  : {highest_mark:.2f}")
print(f"Lowest Mark   : {lowest_mark:.2f}")
print("=" * 60)

# ==========================
# Student Search
# ==========================

while True:
    search = input("\nEnter student name to search (or 'exit' to quit): ")

    if search.lower() == "exit":
        print("Program ended.")
        break

    found = False

    for student in results:
        if student["name"].lower() == search.lower():
            print("\nStudent Found")
            print("----------------------")
            print(f"Name    : {student['name']}")
            print(f"Average : {student['average']:.2f}")
            print(f"Grade   : {student['grade']}")
            print(f"Status  : {student['status']}")
            found = True
            break

    if not found:
        print("Student not found.")
