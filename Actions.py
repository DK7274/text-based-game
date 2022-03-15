import Rooms
import Enemy
def findAction(action):
    match action:
        case  "inspect room":
            print(Rooms.roomDesc)
        case "go up" | "up":
            if Rooms.currentRoom < 5:
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
            interact = input("what do you want to interact with?")
