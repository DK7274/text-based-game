import Actions
import Items
currentRoom = 1
roomDesc = 1
allowedInteract = 1
global roomLight
roomLight = 0
global crateOpen
global buttonOn
buttonOn = 0
global Lever1
Lever1 = 0
global Lever2
Lever2 = 0
global Lever3
Lever3 = 0
global puzzleOpen
puzzleOpen = 0
global repeatDisable
repeatDisable = 1
global doorOpen
doorOpen = 0
def roomOne():
    global roomDesc
    global allowedInteract
    roomDesc = "you are in a hotel lobby, with an elevator at the north end, and a reception desk with a small sign on it"
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
def roomFour():
    global roomDesc
    global allowedInteract
    global buttonOn
    global puzzleOpen
    global repeatDisable
    global doorOpen
    if Lever1 == 1 and Lever2 == 0 and Lever3 == 1 and repeatDisable == 1:
        print("you hear a dull rumbling, and a light above the button starts growing brightly.")
        buttonOn = 1
        repeatDisable = 0
        doorOpen = 1
    roomDesc = "You are in a large chamber, a locked security door blocking your path. \nThere a three levers to the left of the door, and a button to the right"
    if buttonOn == 0:
        allowedInteract = ["Button","Lever1","Lever2","Lever3"]
    if buttonOn == 1:
        allowedInteract = ["Button"]
def roomChecker():
    if currentRoom == 1:
        roomOne()
    elif currentRoom == 2:
        roomTwo()
    #elif currentRoom == 3:
     #   roomThree()
    elif currentRoom == 4:
        roomFour()
    #elif currentRoom == 5:
     #   roomFive()
