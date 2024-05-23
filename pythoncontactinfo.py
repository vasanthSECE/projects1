import json

# Initialize contacts storage (simulating a database)
contacts = []

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    save_contacts()
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if term.lower() in contact['name'].lower() or term in contact['phone']]
    if found_contacts:
        for idx, contact in enumerate(found_contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
    else:
        print("No matching contacts found.")

def update_contact():
    term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if term.lower() in contact['name'].lower() or term in contact['phone']:
            print(f"Updating contact: {contact['name']} - {contact['phone']}")
            contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']
            save_contacts()
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    term = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if term.lower() in contact['name'].lower() or term in contact['phone']:
            print(f"Deleting contact: {contact['name']} - {contact['phone']}")
            contacts.remove(contact)
            save_contacts()
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
