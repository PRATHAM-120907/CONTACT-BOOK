contacts = {}

while True:
    print('\n CONTACT BOOK APP')
    print("1) CREATE CONTACT")
    print("2) VIEW CONTACT")
    print("3) UPDATE CONTACT")
    print("4) DELETE CONTACT")
    print("5) SEARCH CONTACT")
    print("6) COUNT CONTACT")
    print("7) EXIT CONTACT")

    choice = int(input("ENTER YOUR CHOICE ="))

    if choice == 1:
        name = input("ENTER THE NAME = ")
        if name in contacts:
            print(f"the name {name} already exists in the list ")
        else:
            age = int(input("ENTER THE AGE = "))
            email = input("ENTER THE EMAIL= ")
            mobile = input("ENTER THE MOBILE NUMBER = ")
            contacts[name] = {'name': name, 'age': age, 'email': email, 'mobile': mobile}
            print(f"CONTACT NAME {name} HAS BEEN ADDED SUCCESSFULLY !!")

    elif choice == 2:
        name = input("ENTER THE NAME TO VIEW = ")
        if name in contacts:
            contact = contacts[name]
            print(f"name: {name}, age: {contacts[name]['age']}, mobile: {contacts[name]['mobile']}")
            
        else:
            print("CONTACT NOT FOUND !")

    elif choice == 3:
        name = input("ENTER THE NAME TO UPDATE = ")
        if name in contacts:
            age = int(input("ENTER UPDATED AGE = "))
            email = input("ENTER THE UPDATED EMAIL= ")
            mobile = input("ENTER THE UPDATED MOBILE NUMBER = ")
            contacts[name] = {'name': name, 'age': age, 'email': email, 'mobile': mobile}
        else:
            print("CONTACT NOT FOUND !")

    elif choice == 4:
        name = input("ENTER THE NAME TO DELETE = ")
        if name in contacts:
            del contacts[name]
            print(f"{name} has been deleted")
        else:
            print("CONTACT NOT FOUND")

    elif choice == 5:
        search_name = input("ENTER THE NAME TO SEARCH = ")
        if search_name in contacts:
            print(f"name: {search_name}, age: {contacts[search_name]['age']}, mobile: {contacts[search_name]['mobile']}")
        else:
            print("Contact not found.")

    elif choice == 6:
        print(f"THE TOTAL NUMBER IN CONTACTS ARE = {len(contacts)} ")

    elif choice == 7:
        print("CLOSING THE PROGRAM...")
        break

    else:
        print("INVALID INPUT")
