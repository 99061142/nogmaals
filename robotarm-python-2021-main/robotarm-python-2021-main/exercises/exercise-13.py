from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

checking = True
blocks = 1

while checking:
    robotArm.grab()
    color = robotArm.scan()

    if color == "":
        checking = False
        
        for i in range(blocks - 1):
            robotArm.moveRight()
    
    
    else:   
        for i in range(blocks):
            robotArm.moveRight()
        
        robotArm.drop()
        
        for i in range(blocks):
            robotArm.moveLeft()

        blocks += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()