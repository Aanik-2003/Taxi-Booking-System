# empty list to store contact details

contacts = []

# function to add new contact
def add_contact(name, phone, email):
    contact = {f"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"New contact has been added by {name}")

# function to view all contacts
def view_all_contacts():
    if not contacts:
        print("No contacts to show!")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# function to search contact
def search_contact(user_name):
    for contact in contacts:
        if user_name in contact['name']:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            break
        else:
            print("Contact not found!")

# Main program
if __name__ == "__main__":

    while True:
        print(f"---------------------------------------")
        print("  Welcome To Contact Management System")
        print(f"---------------------------------------")

        print("Choose Any Options: \n"
              "1. Add new contact \n"
              "2. View all contacts \n"
              "3. Search contact \n"
              "4. Exit program")

        user_input = int(input("Enter any options: "))
        if user_input == 1:
            user_name = input("Enter your name: ")
            user_phone = int(input("Enter your phone number: "))
            user_email = input("Enter your email: ")

            add_contact(user_name, user_phone, user_email)

        elif user_input == 2:
            view_all_contacts()

        elif user_input == 3:
            user_name = input("Enter your name: ")
            search_contact(user_name)

        elif user_input == 4:
            break
        else:
            print("Enter valid option!")

