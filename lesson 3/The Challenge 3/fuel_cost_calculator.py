# ====================================
# South African Fuel Cost Calculator
# ====================================

print("====================================")
print(" SOUTH AFRICAN FUEL COST CALCULATOR ")
print("====================================")

# Ask the user for input
kilometers = float(input("Enter the number of kilometers to travel: "))
petrol_price = float(input("Enter the petrol price per litre (R): "))

# Calculate fuel needed
liters_needed = kilometers / 10

# Calculate total fuel cost
total_cost = liters_needed * petrol_price

# Round the total cost to 2 decimal places
total_cost = round(total_cost, 2)

# Display the results
print("\n====================================")
print("           TRIP SUMMARY")
print("====================================")
print(f"Distance:           {kilometers:.2f} km")
print(f"Fuel Needed:        {liters_needed:.2f} litres")
print(f"Petrol Price:       R{petrol_price:.2f}")
print(f"Total Fuel Cost:    R{total_cost:.2f}")
print("====================================")
print("Thank you! Drive safely.")
print("====================================")
