<img width="1067" height="685" alt="image" src="https://github.com/user-attachments/assets/ce38695b-702b-4cd1-824d-6b40fb6706e0" />


# Student Info Formatter

# Collect user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Combine first name and surname
full_name = f"{first_name} {surname}"

# Display greeting
print(f"\nWelcome, {full_name}!")

# Display name in different formats
print(f"Name in UPPERCASE: {full_name.upper()}")
print(f"Name in Title Case: {full_name.title()}")

# Calculate age in months
age_in_months = age * 12
print(f"Age in Months: {age_in_months}")

# Round favourite number
rounded_number = round(favourite_number, 2)
print(f"Favourite Number (Rounded): {rounded_number}")

# Display data types
print("\nData Types")
print(f"First Name: {type(first_name)}")
print(f"Surname: {type(surname)}")
print(f"Age: {type(age)}")
print(f"Favourite Number: {type(favourite_number)}")


---

---

#output
---

<img width="1172" height="512" alt="image" src="https://github.com/user-attachments/assets/8ed0014d-feb6-4d3f-813b-e4da57de1a99" />
