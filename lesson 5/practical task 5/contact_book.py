

# contact_book.py

# List to store contacts
contacts = []


# Function to add a contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("\nContact added successfully!\n")


# Function to search for a contact
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


# Function to delete a contact
def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("\nContact deleted successfully!\n")
            return

    print("\nContact not found.\n")


# Function to display all contacts
def view_all():
    if len(contacts) == 0:
        print("\nNo contacts available.\n")
    else:
        print("\n----- Contact List -----")
        for contact in contacts:
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 25)


# Main Menu
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter name to search: ")
        result = search_contact(name)

        if result:
            print("\nContact Found:")
            print(f"Name : {result['name']}")
            print(f"Phone: {result['phone']}")
            print(f"Email: {result['email']}\n")
        else:
            print("\nContact not found.\n")

    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("\nInvalid choice. Please select a number between 1 and 5.\n")
