import random 

def start_game():
    """Starting the adventure game."""

    print("Welcome to Omar's Adventure!")
    print("You start by waking up in heaven, what would you do?")

    while True:
        action = input("> ").lower()

        if action == "Look around":
            print("You observe your surroundings and see that there's so much around you.")
        elif action == "go north":
            print("You go north and follow your dreams in the forest. what comes next is all up to you")
        if action == "go south": 
            print("You run into an ogre waiting to eat your blood like crazy.")
            break
        else: 
            print("I don't really know what the heck you're trying to input here.")

    if __name__ == "__main__":
        start_game()