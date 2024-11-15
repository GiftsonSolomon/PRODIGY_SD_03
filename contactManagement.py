contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        print("This contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-------------------")

def update_contact():
    name = input("Enter the contact name to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input("Enter new phone number: ")
    email = input("Enter new email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' updated successfully!")

def delete_contact():
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

def search_contact():
    name = input("Enter the contact name to search for: ")
    if name in contacts:
        print("\n--- Contact Found ---")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
