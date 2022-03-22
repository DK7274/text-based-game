import Actions
import Items
import Enemy
currentRoom = 1
roomDesc = 1
allowedInteract = 1
allowedPickup = 1
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
global gunTake
gunTake = 0
enemySetUp = 1
bossSetUp = 1
def roomOne(): #setup for the first room
    global roomDesc
    global allowedInteract
    roomDesc = "you are in a hotel lobby, with an elevator at the north end, and a reception desk with a small sign on it" #description for first room
    allowedInteract = [Items.signRoomOneName] #experimentation with variables instead of strings
def roomTwo(): #setup for the second room
    global roomDesc
    global allowedInteract
    global allowedPickup
    if roomLight == 0: #if light is off, you cannot open the crate
        roomDesc = "you are in a darkened room, there is a light switch on the wall beside the elevator. You can see a large rectangular box in the center of the room "
        if Items.crateOpen == 0:
            allowedInteract = ["Light Switch", "Box"]
        else: #removes interaction option with box if it has already been opened
            allowedInteract = ["Light Switch"]

    if roomLight == 1: #allows you to interact with the crate if the light is on
        roomDesc = "you are in a room with a dim bulb lighting it. Shadows flicker along the edges where the walls meet the floor. There is a green crate in the centre of the room."
        if Items.crateOpen == 0:
            allowedInteract = ["Light Switch", "Crate"]
        elif gunTake == 0: # takes the gun and crate out of the array if it has already been opened
            allowedInteract = ["Light Switch", "Gun"]
        else:
            allowedInteract = ["Light Switch"]
def roomThree():
    global enemySetUp
    global roomDesc
    if enemySetUp == 1:
        Enemy.enemyCount = 2
        enemySetUp = 0
    if Enemy.enemyCount == 2:
        roomDesc = "As you enter the room, you see two cyborg bandits.\ntheir hands move towards their holsters"
    elif Enemy.enemyCount == 1:
        roomDesc = "One of the cyborgs is laying on the floor, riddled with bullet holes, the other is still standing defiantly"
    elif Enemy.enemyCount == 0:
        roomDesc = "The bloody and battered bodies of two cyborgs lay, broken, on the floor. You can see the lights slowly dying in their eyes."

def roomFour():
    global roomDesc
    global allowedInteract
    global buttonOn
    global puzzleOpen
    global repeatDisable
    global doorOpen
    if Lever1 == 1 and Lever2 == 0 and Lever3 == 1 and repeatDisable == 1: #if the correct code is input, unlocks the button
        print("you hear a dull rumbling, and a light above the button starts growing brightly.")
        buttonOn = 1
        repeatDisable = 0 #stops the print in this if statement being repeated every time you interact with this room
        doorOpen = 1
        roomDesc = "You are in a large chamber, a once locked security door blocking your path\nThe elevator stands ominousy at the end of the room."
    roomDesc = "You are in a large chamber, a locked security door blocking your path. \nThere a three levers to the left of the door, and a button to the right"
    if buttonOn == 0: #if button is not activated, make you able to input the code
        allowedInteract = ["Button","Lever1","Lever2","Lever3"]
    if buttonOn == 1: #if button is on, you cannot change the lever code, just press the button
        allowedInteract = ["Button"]
def roomFive():
    global bossSetUp
    global roomDesc
    roomDesc = "In this room, there is a large robot, wielding a gun."
    if bossSetUp == 1:
        Enemy.bossHere = 1
        bossSetUp = 0
def roomChecker(): #code that checks the room and runs the function for each seperate room.
    if currentRoom == 1:
        roomOne()
    elif currentRoom == 2:
        roomTwo()
    elif currentRoom == 3:
        roomThree()
    elif currentRoom == 4:
        roomFour()
    elif currentRoom == 5:
        roomFive()