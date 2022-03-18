import Items
import Rooms
import Enemy
import time
global interact
def findAction(action):
    match action:
        case "inspect":
            print(Rooms.roomDesc)
        case "go up" | "up":
            if Rooms.currentRoom == 4 and Rooms.doorOpen == 0:
                    print("The door blocks your way, you cannot go any further.")
            elif Rooms.currentRoom < 5:
                print("penis")
                if Enemy.enemyCount == 0:
                    Rooms.currentRoom = Rooms.currentRoom + 1
                    Rooms.roomChecker()
                    print("you move up a floor, you are now on floor " + str(Rooms.currentRoom))
                    print(Rooms.roomDesc)
                else:
                    print("you cannot leave yet, there's more killing to do!")
            else:
                print("you are at the top floor, you cannot go any higher!")
        case "go down" | "down":
            if Rooms.currentRoom > 1:
                if Enemy.enemyCount == 0:
                    Rooms.currentRoom = Rooms.currentRoom - 1
                    Rooms.roomChecker()
                    print("you move down a floor, you are now on floor " + str(Rooms.currentRoom))
                    print(Rooms.roomDesc)
                else:
                    print("you cannot leave yet, there's more killing to do!")
            else:
                print("you are on the bottom floor, you cannot go any lower")
        case "interact":
            print("you can interact with")
            print( ','.join(Rooms.allowedInteract))
            interact = input("what do you want to interact with?\n")
            for a in range(len(Rooms.allowedInteract)):
                if interact == Rooms.allowedInteract[a]:
                    Items.itemChecker(interact)
        case "quit":
            print("game quitting! please play again another time!")
            time.sleep(5)
            exit()
    Rooms.roomChecker()