import Rooms
import Actions
import time
global gameRun
gameRun = 1
Rooms.roomChecker() #calls checking the room to set the room description
print("welcome to CyberSpunk 2023! a technologically advanced futuristic city where dreams are made of (or crushed")
menu = input("what do you want to do?\n") #interaction with the menu
match menu:
    case "start" | "begin" | "play":  #if input is play then it starts game
        startGame = input("do you want to know how to play?\n") #asks if you want to know how to play
        if startGame == "yes": # if yes, gives description of how to play
            print("to play CyberSpunk 2023, you must input simple text commands to control your character, defeat enemies,")
            print("and use your inventory. Use simple commands such as 'up' to go upand 'interact' in order to command your character!\n \n")
        print(Rooms.roomDesc) #if not, doesnt give instructions, both choices continue game as normal
    case "quit": #quitting from the menu
        gameRun = 3
while gameRun == 1: #code that calls the code that makes the action be asked for
    action = input("what do you want to do next?\n")
    Actions.findAction(action)
    if gameRun == 3: # code for qutting from menu after called
        print("game quitting! please play again another time!")
        time.sleep(5)
        exit()