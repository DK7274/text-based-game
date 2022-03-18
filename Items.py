import Rooms
import Actions
signRoomOneDesc= "you approach the sign and read it. it reads: 'ATTENTION: BUILDING HARBORS DANGEROUS FUGITIVES. CLIMB AT YOUR OWN RISK'" #setting description and name for sign in room 1
signRoomOneName = "sign"
global crateOpen
crateOpen = 0
def roomInteract1(itemInteract1): #code for first room interaction
    match itemInteract1:
        case "sign": #if input is sign then print what is on the sign
            print(signRoomOneDesc)
def roomInteract2(itemInteract2): #code for the second room interaction
    match itemInteract2:
        case "Light Switch":
            if Rooms.roomLight == 1: #if lifht switch is on turn it off
                print("you flip the light switch")
                Rooms.roomLight = 0
                Actions.interact = "reset" #make the code not run both the if and the else statement at the same time
            else:
                print("you flip the light switch") #if the light switch is off turn it on
                print("a lightbulb flickers on in the room, revealing the box is a large crate, with a bolt on it")
                Rooms.roomLight = 1
                Actions.interact = "reset"

        case "Box": #code for not being able to open the crate in the dark
                print("you feel your way over to the box, stumbling on small imperfections in the floor along the way. When you reach\n it, you attempt to open the lid but it refuses to budge")
        case "Crate": #code for opening the crate in the light
            print("you open the bolt and heave open the crate, inside is a small pistol, and a note reading \n 'you will need this where you are going'")
            global crateOpen
            crateOpen = 1
def roomInteract4(itemInteract4): #interaction in room 4
    match itemInteract4:
        case "Lever1": #first lever
            if Rooms.Lever1 == 0: #if lever down then it turns up
                print("You flip the first lever up, you hear a slight buzz behind the wall.")
                Rooms.Lever1 = 1
            else:
                print("you flip the first lever back down.") #if lever up then turns it down
                Rooms.Lever1 = 0
        case "Lever2": #second lever
            if Rooms.Lever2 == 0:  #if lever down turns it up
                print("You flip the second lever up.")
                Rooms.Lever2 = 1
            else: #if lever up then it turns down
                print("You flip the second lever down, you hear a slight buzz behind the wall.")
                Rooms.Lever2 = 0
        case "Lever3": #third lever
            if Rooms.Lever3 == 0: #if lever down turns up
                print("You flip the third lever up, you hear a slight buzz behind the wall.")
                Rooms.Lever3 = 1
            else: # if lever up turns down
                print("You flip the third lever down")
                Rooms.Lever3 = 0
        case "Button": # interaction with button
            if Rooms.buttonOn == 0: #if the lever code isnt working then button cannot open door
                print("You push the button and nothing happens")
            if Rooms.buttonOn == 1: #if lever code is working then it opens the door
                print("The door slowly rumbles and opens, revealing the elevator to the final floor.\n There is a skull on the button to the next floor.")
                Rooms.doorOpen = 1
def itemChecker(itemInteract): #checks what room you are in, makes code less complicated, computer doesnt have to sort through the entire list of items
    if Rooms.currentRoom == 1:
        roomInteract1(itemInteract)
    if Rooms.currentRoom == 2:
        roomInteract2(itemInteract)
    if Rooms.currentRoom == 4:
        roomInteract4(itemInteract)