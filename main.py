import Rooms
import Actions
import time
gameRun = 1
Rooms.roomChecker()
print("welcome to CyberSpunk 2023! a technologically advanced futuristic city where dreams are made of (or crushed")
menu = input("what do you want to do?\n")
match menu:
    case "start" | "begin" | "play":
        startGame = input("do you want to know how to play?\n")
        if startGame == "yes":
            print("to play CyberSpunk 2023, you must input simple text commands to control your character, defeat enemies,")
            print("and use your inventory. Use simple commands such as move to (blank) and pick up (blank) in order to command your character!\n \n")
        print(Rooms.roomDesc)
    case "quit":
        gameRun = 3
while gameRun == 1:
    action = input("what do you want to do next?\n")
    Actions.findAction(action)
if gameRun == 2:
    print("congratulations! you have beaten the game! Mr Groom give me an A.")
    time.sleep(5)
    exit()
elif gameRun == 3:
    print("game quitting! please play again another time!")
    time.sleep(5)
    exit()
