

# ====================================
# Username and Message Formatter
# ====================================

print("====================================")
print("   USERNAME AND MESSAGE FORMATTER")
print("====================================")

# Collect user information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio: ")

# Create username
username = (first_name[0] + last_name).lower()

# Format full name
full_name = f"{first_name} {last_name}".title()

# Clean the bio
clean_bio = bio.strip()

# Count characters
bio_length = len(clean_bio)

# Replace "I am" with "I'm"
updated_bio = clean_bio.replace("I am", "I'm")

# Display results
print("\n====================================")
print("         USER PROFILE")
print("====================================")
print(f"Username : {username}")
print(f"Full Name: {full_name}")
print(f"Bio      : {updated_bio}")
print(f"Characters in Bio: {bio_length}")
print("====================================")
