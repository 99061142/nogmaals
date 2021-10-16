from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

moveLeft_amount = 8
moveRight_amount = 9

for i in range(5):
    robotArm.grab()

    for i in range(moveRight_amount):
        robotArm.moveRight()

    robotArm.drop()

    for i in range(moveLeft_amount): 
        robotArm.moveLeft()

    moveLeft_amount -= 2
    moveRight_amount -= 2

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()