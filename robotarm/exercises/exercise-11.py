from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:

for i in range(8):
    robotArm.moveRight()

for i in range(9):
    robotArm.grab()

    color = robotArm.scan()

    if color != "white":
        robotArm.drop()
    
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()

    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

