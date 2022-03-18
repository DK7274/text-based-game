import Items
import Rooms
import Enemy
import time
global interact
def findAction(action): #function for finding any action you are doing
    match action:
        case "inspect": #inspection action for checking the current room description
            print(Rooms.roomDesc)
        case "go up" | "up": #code for going up a room
            if Rooms.currentRoom == 4 and Rooms.doorOpen == 0: #this code makes sure that you have unlocked the puzzle on floor 4 before it allows you to go to floor 5
                    print("The door blocks your way, you cannot go any further.")
            elif Rooms.currentRoom < 5: #checks you are below room 5
                if Enemy.enemyCount == 0: #checks that there are no enemies on your current floor
                    Rooms.currentRoom = Rooms.currentRoom + 1
                    Rooms.roomChecker()
                    print("you move up a floor, you are now on floor " + str(Rooms.currentRoom))
                    print(Rooms.roomDesc)
                else:
                    print("you cannot leave yet, there's more killing to do!") #if enemies are on current floor, you cannot leave
            else:
                print("you are at the top floor, you cannot go any higher!") #prevents you from going above the uppermost floor
        case "go down" | "down": #code for going down a room
            if Rooms.currentRoom > 1: #checks you are above floor 1
                if Enemy.enemyCount == 0:
                    Rooms.currentRoom = Rooms.currentRoom - 1
                    Rooms.roomChecker()
                    print("you move down a floor, you are now on floor " + str(Rooms.currentRoom))
                    print(Rooms.roomDesc)
                else:
                    print("you cannot leave yet, there's more killing to do!") #cannot leave if enemies here
            else:
                print("you are on the bottom floor, you cannot go any lower") #prevents you from going below the lowest floor
        case "interact": #code for interacting with objects in the room
            print("you can interact with")
            print( ','.join(Rooms.allowedInteract)) #joins the array so its not in the [] brackets
            interact = input("what do you want to interact with?\n") #asks what you want to interact with
            for a in range(len(Rooms.allowedInteract)):
                if interact == Rooms.allowedInteract[a]:
                    Items.itemChecker(interact) #if item is in array for allowedInteract, allows you to interact with it
        case "quit": #alternate code for quitting while normally playing the game
            print("game quitting! please play again another time!")
            time.sleep(5)
            exit()
    Rooms.roomChecker() #checks room every time function is run so that the description of room stays up to date