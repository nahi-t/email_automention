def add_person():
    new_people = []
    for i in range(3):  # to add 3 contacts as your message says
        print(f"Input contact #{i+1}")
        name = input("Name: ")
        age = input("Age: ")
        email = input("Email: ")

        person = {
            "name": name,
            "age": age,
            "email": email
        }
        new_people.append(person)

    return new_people


def delete_person(people):
    if not people:
        print("No contacts to delete.")
        return

    print("\nContacts:")
    for i, person in enumerate(people):
        print(f"{i + 1} - {person['name']} | {person['age']} | {person['email']}")

    try:
        choice = int(input("Enter the number of the contact to delete: "))
        if 1 <= choice <= len(people):
            removed = people.pop(choice - 1)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


print("Hi, welcome to the contact management system!\n")
print("You can add, delete, search, and view contacts.")

people = []
commands = input("Please enter a command: add, delete, search, q for quit: ").lower()

while True:
    if commands == "add":
        print("You can add 3 contacts")
        new_people = add_person()
        people.extend(new_people)
        print("You have added", len(new_people), "contacts.")
        print("Total contacts:", len(people))

    elif commands == "delete":
        delete_person(people)

    elif commands == "search":
        # implement search later
        pass

    elif commands == "q":
        print("Thank you for using the contact management system")
        break

    else:
        print("You can only add, delete, search, and view contacts")

    commands = input("\nEnter next command: add, delete, search, q for quit: ").lower()
