# Phone Directory Search

# Step 1: Create a dictionary with 3 contacts
contacts = {
    "Alice": "0821112222",
    "Bob": "0833334444",
    "Charlie": "0845556666"
}

# Step 2: Ask the user for the friend's name
name = input("Enter the name of the friend to look up: ")

# Step 3 & 4: Check if the contact exists
if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")
