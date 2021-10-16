from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:

moveLeft_amount = 8
moveRight_amount = 9

for i in range(9):
    robotArm.grab()

    color = robotArm.scan()

    if color != "red":
        robotArm.drop()
        robotArm.moveRight()
    
    else:
        for i in range(moveRight_amount):
            robotArm.moveRight()

        robotArm.drop()
        
        for i in range(moveLeft_amount):
            robotArm.moveLeft()

    moveLeft_amount -= 1
    moveRight_amount -= 1
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()