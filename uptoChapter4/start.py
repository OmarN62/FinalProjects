def nameTake():
    print("What's your name:")
    #print(len(name))
    name = input()
    if len(name) <= 10:   
        print("Your name is a normal length of characters")
        print("Your name is: " + name)
    elif name >= 10: 
        print("Your name isn't that normal of a length, why don't you come up with a new one:")
        name2 = input()
        print("Your new name is, " + name2)
    else:
        print("Your name is, " + name)
nameTake()
