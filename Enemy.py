import random
enemyCount = 0 #placeholder for enemy count so that I could test out restricting movement between rooms
bossHere = 0
playerHealth = 100
playerDamage = random.randint(10, 20)
enemy1Health = 50
enemy1Damage = random.randint(0, 15)
enemy2Health = 50
enemy2Damage = random.randint(0, 15)
bossHealth = 150
bossDamage = random.randint(0,30)
def resetDamage():
    global playerDamage
    global enemy1Damage
    global enemy2Damage
    global bossDamage
    playerDamage = random.randint(10,20)
    enemy1Damage = random.randint(0,15)
    enemy2Damage = random.randint(0,15)
    bossDamage = random.randint(0,30)