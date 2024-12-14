import sys

while True:
    print("This is code is true")
    response = input()
    if response == "not true":
        sys.exit()
    print("You typed" + response)