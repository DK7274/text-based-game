import Rooms
import Actions
signRoomOneDesc= "you approach the sign and read it. it reads: 'ATTENTION: BUILDING HARBORS DANGEROUS FUGITIVES. CLIMB AT YOUR OWN RISK'"
signRoomOneName = "sign"
def roomInteract1(itemInteract1):
    match itemInteract1:
        case "sign":
            print(signRoomOneDesc)
def itemChecker(itemInteract):
    if Rooms.currentRoom == 1:
        roomInteract1(itemInteract)