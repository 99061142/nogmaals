# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()

for i in range(7):
    robotArm.grab()

    for i in range(8):
        robotArm.moveRight()

    robotArm.drop()

    for i in range(8):
        robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()