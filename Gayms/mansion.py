import time

# Define game functions
def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("Welcome to Mystery Mansion!")
    print_pause("You are standing at the entrance of a mysterious mansion.")
    print_pause("Your goal is to find the key to the front door and escape.")
    print_pause("But be careful - there are many dangers lurking inside...")
    print_pause("Are you ready to begin?")

def choose_location():
    print_pause("Where would you like to go?")
    print_pause("1. Living Room")
    print_pause("2. Kitchen")
    print_pause("3. Library")
    print_pause("4. Secret Room")
    print_pause("5. Quit Game")

    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        living_room()
    elif choice == '2':
        kitchen()
    elif choice == '3':
        library()
    elif choice == '4':
        secret_room()
    elif choice == '5':
        quit_game()
    else:
        print_pause("Sorry, I didn't understand that.")
        choose_location()

def living_room():
    print_pause("You are now in the living room.")
    if "living room key" not in inventory:
        print_pause("There is a key on the table.")
        inventory.append("living room key")
    else:
        print_pause("There is nothing else here.")
    choose_location()

def kitchen():
    print_pause("You are now in the kitchen.")
    if "knife" not in inventory:
        print_pause("There is a knife on the counter.")
        inventory.append("knife")
    else:
        print_pause("There is nothing else here.")
    choose_location()

def library():
    print_pause("You are now in the library.")
    if "book" not in inventory:
        print_pause("There is a book on the shelf.")
        inventory.append("book")
    else:
        print_pause("There is nothing else here.")
    choose_location()

def secret_room():
    print_pause("You are now in the secret room.")
    if "front door key" not in inventory:
        print_pause("There is a safe in the corner of the room.")
        if "safe code" in inventory:
            print_pause("You enter the code and the safe opens.")
            print_pause("Inside is the key to the front door!")
            inventory.append("front door key")
        else:
            print_pause("The safe is locked.")
    else:
        print_pause("There is nothing else here.")
    choose_location()

def quit_game():
    print_pause("Thanks for playing Mystery Mansion!")
    print_pause("See you next time.")
    quit()

# Start the game
inventory = []
intro()
choose_location()
