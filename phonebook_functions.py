phonebook_dictionary = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923',
    'James': '546-756-987',
    'Marge': '645-934-3425'
}

running = True

def look_up(name_number):
    if user_input == 1:
        name = input("Name: ")
        names_found = []
        if name in phonebook_dictionary:
            print("")
            print("Name: " + name + " Phone Number: " + phonebook_dictionary[name])
            print("")
        else:
            print("")
            print(name + " not found.")
            print("")
    return

def set_new(name_number):
    if user_input == 2:
        name = input("New name: ")
        phone_number = input("New phone number: ")
        phonebook_dictionary[name] = phone_number
        print("")
        print("New entry, " + name + ", has been stored.")
        print("")
    return

def delete(name_number):
    if user_input == 3:
        name = input("Name to delete info: ")
    if name in phonebook_dictionary:
        del phonebook_dictionary[name]
        print("")
        print(name + " was deleted.")
        print("")
    else:
        print("")
        print("Name was not found")
        print("")
    return

def list_all(name_number):
    if user_input == 4:
        print("")
        print(phonebook_dictionary)
        print("")
    return

def quit():
    if user_input == 5:
        print("")
        print("Thank you for using Zach's Phonebook Directory")
        print("")
        running = False
    return

while running == True:
    print("""
Electronic Phone Book
---------------------
1. Look up an entry
2. Set a new entry
3. Delete an entry
4. List all entries
5. Quit
""")
  
    user_input = int(input("What do you want to do (1-5)? "))

# Looking up an entry
    
    if user_input == 1:
        print(look_up(input))


# Setting a new entry
    elif user_input == 2:
        print(set_new(input))

# Deleting an entry
    elif user_input == 3:
        print(delete(input))


# Listing all entries
    elif user_input == 4:
        print(list_all(input))

# Quitting the menu
    elif user_input == 5:
        print(quit())
        break
