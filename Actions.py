import Items
import Rooms
import Enemy
import time
global interact
import NewBackpack
import random
def findAction(action): #function for finding any action you are doing
    match action:
        case "inspect": #inspection action for checking the current room description
            print(Rooms.roomDesc)
        case "attack": #attack action
            if Enemy.enemyCount == 0 and Enemy.bossHere == 0: #if there is no enemy or boss, you cannot attack.
                print("there is no enemy here, you cannot attack!")
            elif Enemy.enemyCount == 1 or 2: #checks if there is an enemy
                attack = input("Who do you want to attack?\n Enemy 1 or Enemy 2?\n")
                if attack == "Enemy 1": #if you attack the first enemy
                    if Enemy.enemy1Health <= 0: #if enemy is alreay dead, cannot attack
                        print("This enemy is already dead!")
                    else: #attack damage for enemy
                        Enemy.enemy1Health =Enemy.enemy1Health - Enemy.playerDamage
                        print("You hit Enemy 1 for " + str(Enemy.playerDamage) + "!\nIts health is now " + str(Enemy.enemy1Health))
                        Enemy.resetDamage() #function to reset damage because it doesnt reset automatically
                        if Enemy.enemy1Health <= 0: #if you get the enemy to 0 or below, then you kill it
                            print("You kill Enemy 1!")
                            Enemy.enemyCount = Enemy.enemyCount - 1 #clears enemy from enemy count
                        else:
                            Enemy.playerHealth = Enemy.playerHealth - Enemy.enemy1Damage #enemy fights back
                            print("Enemy 1 hits you for " + str(Enemy.enemy1Damage) +" !\n you now have " + str(Enemy.playerHealth) + " Health left!")
                            if Enemy.playerHealth <= 0: #if it kills you, game over
                                dieGameOver()
                if attack == "Enemy 2": #if you attack the second enemy, a copy of the enemy 1 code with enemy 2 inserted into it
                    if Enemy.enemy2Health <= 0: #cannot attack if enemy already dead
                        print("This enemy is already dead!")
                    else:
                        Enemy.enemy2Health =Enemy.enemy2Health - Enemy.playerDamage
                        print("You hit Enemy 2 for " + str(Enemy.playerDamage) + "!\nIts health is now " + str(Enemy.enemy2Health))
                        Enemy.resetDamage()
                        if Enemy.enemy2Health <= 0:
                            print("You kill Enemy 2!")
                            Enemy.enemyCount = Enemy.enemyCount - 1
                        else:
                            Enemy.playerHealth = Enemy.playerHealth - Enemy.enemy2Damage
                            print("Enemy 2 hits you for " + str(Enemy.enemy2Damage) +" !\n you now have " + str(Enemy.playerHealth) + " Health left!")
                            if Enemy.playerHealth <= 0:
                                dieGameOver()
        case "go up" | "up": #code for going up a room
            if Rooms.currentRoom == 4 and Rooms.doorOpen == 0: #this code makes sure that you have unlocked the puzzle on floor 4 before it allows you to go to floor 5
                    print("The door blocks your way, you cannot go any further.")
            elif Rooms.currentRoom < 5: #checks you are below room 5
                if Enemy.enemyCount == 0: #checks that there are no enemies on your current floor
                    Rooms.currentRoom = Rooms.currentRoom + 1
                    Rooms.roomChecker()
                    print("you move up a floor, you are now on floor " + str(Rooms.currentRoom))
                    print(Rooms.roomDesc)
                else:
                    print("you cannot leave yet, there's more killing to do!") #if enemies are on current floor, you cannot leave
            else:
                print("you are at the top floor, you cannot go any higher!") #prevents you from going above the uppermost floor
        case "go down" | "down": #code for going down a room
            if Rooms.currentRoom > 1: #checks you are above floor 1
                if Enemy.enemyCount == 0:
                    Rooms.currentRoom = Rooms.currentRoom - 1
                    Rooms.roomChecker()
                    print("you move down a floor, you are now on floor " + str(Rooms.currentRoom))
                    print(Rooms.roomDesc)
                else:
                    print("you cannot leave yet, there's more killing to do!") #cannot leave if enemies here
            else:
                print("you are on the bottom floor, you cannot go any lower") #prevents you from going below the lowest floor
        case "interact": #code for interacting with objects in the room
            print("you can interact with")
            print( ','.join(Rooms.allowedInteract)) #joins the array so its not in the [] brackets
            interact = input("what do you want to interact with?\n") #asks what you want to interact with
            for a in range(len(Rooms.allowedInteract)):
                if interact == Rooms.allowedInteract[a]:
                    Items.itemChecker(interact) #if item is in array for allowedInteract, allows you to interact with it
        case "check bag":
            print(NewBackpack.backPack)
        case "quit": #alternate code for quitting while normally playing the game
            print("game quitting! please play again another time!")
            time.sleep(5)
            exit()
    Rooms.roomChecker()  # checks room every time function is run so that the description of room stays up to date
def dieGameOver(): #game over from dying
    print("you died! game over!")
    exit()