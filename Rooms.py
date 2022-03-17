import Actions
import Items
currentRoom = 1
roomDesc = 1
allowedInteract = 1
global roomLight
roomLight = 0
global crateOpen
def roomOne():
    global roomDesc
    global allowedInteract
    roomDesc = "you are in a hotel lobby, with an elevator at the north end, and a reception desk with a small sign on it"
    print(Items.signRoomOneName)
    allowedInteract = [Items.signRoomOneName]
def roomTwo():
    global roomDesc
    global allowedInteract
    if roomLight == 0:
        roomDesc = "you are in a darkened room, there is a light switch on the wall beside the elevator. You can see a large rectangular box in the center of the room "
        if Items.crateOpen == 0:
            allowedInteract = ["Light Switch", "Box"]
        else:
            allowedInteract = ["light Switch"]

    if roomLight == 1:
        roomDesc = "you are in a room with a dim bulb lighting it. Shadows flicker along the edges where the walls meet the floor. There is a green crate in the centre of the room."
        if Items.crateOpen == 0:
            allowedInteract = ["Light Switch", "Crate"]
        else:
            allowedInteract = ["Light Switch"]
def roomChecker():
    if currentRoom == 1:
        roomOne()
    elif currentRoom == 2:
        roomTwo()
    #elif currentRoom == 3:
     #   roomThree()
    #elif currentRoom == 4:
     #   roomFour()
    #elif currentRoom == 5:
     #   roomFive()
