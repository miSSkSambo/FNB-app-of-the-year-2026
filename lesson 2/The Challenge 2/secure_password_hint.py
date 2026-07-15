# ====================================
# Secure Password Hint Tool
# ====================================

print("====================================")
print("    SECURE PASSWORD HINT TOOL")
print("====================================")

# Ask the user to enter their password
password = input("Enter your secret password: ")

# Remove any spaces at the beginning or end
password = password.strip()

# Get the first and last letters
first_letter = password[0]
last_letter = password[-1]

# Display the password hint
print("\n====================================")
print(f"Password Hint: It starts with '{first_letter.upper()}' and ends with '{last_letter.upper()}'.")
print("====================================")
