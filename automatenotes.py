def func():
    name = input("What's your name:")
    age = input("What's your age?:")
    if name == "Alice":
        print("Hi, Alice")
    elif age < 12:
        print("You are not Alice, kiddo")
    elif age > 2000:
        print("Unlike you, Alice is not an undead immortal vampire")
    elif age > 100: 
        print("You are mot Alice, grannie. ")
func()