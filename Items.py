import Rooms
import Actions
signRoomOneDesc= "you approach the sign and read it. it reads: 'ATTENTION: BUILDING HARBORS DANGEROUS FUGITIVES. CLIMB AT YOUR OWN RISK'"
signRoomOneName = "sign"
global crateOpen
crateOpen = 0
def roomInteract1(itemInteract1):
    match itemInteract1:
        case "sign":
            print(signRoomOneDesc)
def roomInteract2(itemInteract2):
    match itemInteract2:
        case "Light Switch":
            if Rooms.roomLight == 1:
                print("you flip the light switch")
                Rooms.roomLight = 0
                Actions.interact = "reset"
            else:
                print("you flip the light switch")
                print("a lightbulb flickers on in the room, revealing the box is a large crate, with a bolt on it")
                Rooms.roomLight = 1
                Actions.interact = "reset"

        case "Box":
                print("you feel your way over to the box, stumbling on small imperfections in the floor along the way. When you reach\n it, you attempt to open the lid but it refuses to budge")
        case "Crate":
            print("you open the bolt and heave open the crate, inside is a small pistol, and a note reading \n 'you will need this where you are going'")
            global crateOpen
            crateOpen = 1
def itemChecker(itemInteract):
    if Rooms.currentRoom == 1:
        roomInteract1(itemInteract)
    if Rooms.currentRoom == 2:
        roomInteract2(itemInteract)