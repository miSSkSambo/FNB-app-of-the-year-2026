

# smart_atm.py

# Fixed bank balance
balance = 500

# Ask the user for the withdrawal amount
withdrawal = float(input("Enter the amount you want to withdraw (R): "))

# Check if the withdrawal amount is valid
if withdrawal <= 0:
    print("Invalid amount. You must withdraw more than R0.")

# Check if there is enough money in the account
elif withdrawal <= balance:
    balance = balance - withdrawal
    print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")

# Otherwise, decline the transaction
else:
    print("Declined. Insufficient funds.")
