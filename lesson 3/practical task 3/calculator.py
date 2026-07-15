# ====================================
# Multi-Function Calculator
# ====================================

print("=" * 40)
print("     MULTI-FUNCTION CALCULATOR")
print("=" * 40)

# Collect two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Handle division safely
if num2 != 0:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)
else:
    division = "Cannot divide by zero"
    floor_division = "Cannot divide by zero"
    modulus = "Cannot divide by zero"

# Display results
print("\n" + "=" * 40)
print("           CALCULATION RESULTS")
print("=" * 40)

print(f"{'Addition:':<20}{addition}")
print(f"{'Subtraction:':<20}{subtraction}")
print(f"{'Multiplication:':<20}{multiplication}")
print(f"{'Division:':<20}{division}")
print(f"{'Floor Division:':<20}{floor_division}")
print(f"{'Modulus:':<20}{modulus}")

print("=" * 40)
print("Thank you for using the calculator!")
print("=" * 40)
