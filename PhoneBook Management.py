file_name = "phonebook.txt"
file1 = open(file_name, "a+")
file1.close


def show_main_menu():
    #main menu for PhoneBook Program
    print("|_______________________________________________________|")
    print("|                  Phone Book Menu                      |\n" +
          "|                *******************                    |\n" +
          "|Enter 1,2,3,4,5 or 6 :-                                |\n" +
          "|Enter 1 To Display Your Contacts Records               |\n" +
          "|Enter 2 To Add a New Contact Record                    |\n" +
          "|Enter 3 To update or Edit Existing Record              |\n" +
          "|Enter 4 To Delete a Contact                            |\n" +
          "|Enter 5 To Search your contacts                        |\n" +
          "|Enter 6 To Quit                                        |\n" +
          "|                 *******************                   |\n" +
          "|_______________________________________________________|")

    choice = input("\n User choice: ")
    if choice == "1":
        file1 = open(file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Phone Book is empty")
        else:
            print(file_contents)
        file1.close
        fn = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        fn = input("Press Enter to continue ...")
        show_main_menu()

    elif choice == "3":
        update_record()
        fn = input("Press Enter to continue ...")
        show_main_menu()

    elif choice == "4":
        delete_record()
        fn = input("Press Enter to continue ...")
        show_main_menu()

    elif choice == "5":
        search_contact_record()
        fn = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "6":
        print("Thanks for using Our Phone Book. ")

    else:
        print("Wrong choice, Please Enter [1 to 6]\n")
        fn = input("Press Enter to continue ...")
        show_main_menu()


def update_record():
    #This function is use for updateing record
    update_name = input("Enter First name to find contact to update: ")
    update_name = update_name.title()
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
    file2 = open(file_name, "w")

    found = False
    for line in file_contents:
        if update_name in line:
            print("Your updating contact record is:", end=" ")
            print(line)
            found = True
            '''updated_name = input("Enter First name for updating contact record: ")
            'new_line = line.replace(update_name,updated_name)'''
            first = input('Enter First Name: ')
            first = first.title()
            last = input('Enter Last Name: ')
            last = last.title()
            phone = input('Enter Phone number: ')
            address = input('Enter Address: ')
            email = input('Enter E-mail: ')
            contact = ("[" + first + " " + last + ", " + phone + ", " + address + ", " + email + "]\n")

            file1.write(contact)
            print(contact)
            break
        elif found == False:
            print("ENTRY NOT FOUND = " + update_name)

    for line in file_contents:
        if line.find(update_name) != -1:
            pass
        else:
            file2.write(line)


def delete_record():
    # This function is use for deleting record
    delete_name = input("Enter First name for Deleting contact record: ")
    delete_name = delete_name.title()
    with open(file_name, 'r') as file:
        lines = file.readlines()

    file1 = open(file_name, "w")
    # file_contents = file1.readlines()
    print("record is deleted")
    for line in lines:
        if line.find(delete_name) != -1:
            pass

        else:
            file1.write(line)



def search_contact_record():
   # This function is used to searches a specific contact record
    search_name = input("Enter First name for Searching contact record: ")

    search_name = search_name.title()
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()

    found = False
    for line in file_contents:

        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("There's no contact Record in Phone Book with name = " + search_name)


def enter_contact_record():
     #It  collects contact info firstname, last name, email, address and phone

    first = input('Enter First Name: ')
    first = first.title()

    last = input('Enter Last Name: ')
    last = last.title()
    phone = (input('Enter Phone number: '))
    address = input('Enter Address: ')
    email = input('Enter E-mail: ')
    contact = ("[" + first + " " + last + ", " + phone + ", " + address + ", " + email + "]\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    print("This contact :\n " + contact + "has been added successfully!")


show_main_menu()
