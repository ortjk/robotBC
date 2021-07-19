import robot
import matplotlib

r = robot.RobotController()
r.connect()

# get to the first marker from spawn
r.left(125)
r.forward(350)

# go left into room at marker
if r.read_marker() == 1:
    r.left(1000)
