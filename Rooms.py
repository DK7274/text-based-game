import Actions
currentRoom = 1
roomDesc = 1
roomLight = 0
allowedInteract = 1
def roomOne():
    global roomDesc
    global allowedInteract
    roomDesc = "you are in a hotel lobby, with an elevator at the north end, and a reception desk with a small sign on it"
    allowedInteract = ["sign","Sign","small sign"]
def roomTwo():
    global roomDesc
    global roomLight
    global allowedInteract
    if roomLight == 0:
        roomDesc = "you are in a darkened room, there is a light switch on the wall beside the elevator. You can see a large rectangular object in the center of the room "
        allowedInteract = ["light switch", "switch", "box"]

    if roomLight == 1:
        roomDesc = "you are in a room with a dim bulb lighting it. Shadows flicker along the edges where the walls meet the floor. There is a green crate in the centre of the room."
        allowedInteract = ["light switch", "switch", "crate", "green crate"]
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
