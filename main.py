import Room1
print("welcome to CyberSpunk 2023! a technologically advanced futuristic city where dreams are made of (or crushed")
menu = input("what do you want to do?\n")
match menu:
    case "start" | "begin" | "play":
        startGame = input("do you want to know how to play?\n")
        if startGame == "yes":
            print("to play CyberSpunk 2023, you must input simple text commands to control your character, defeat enemies,")
            print("and use your inventory. Use simple commands such as move to (blank) and pick up (blank) in order to command your character!")
        else:
            print (Room1.roomOneDesc )