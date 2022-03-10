import Actions
currentRoom = 1
roomDesc = 1
def roomOne():
    global roomDesc
    roomDesc = "you are in a hotel lobby, with an elevator at the north end, and a reception desk with a small sign on it"
def roomTwo():
    global roomDesc
    roomDesc = "you are in a darkened room, there is a light switch on the wall beside the elevator. You can see a large rectangular object along one wall. "
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
