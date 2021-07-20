import robot
from matplotlib import pyplot as plt

r = robot.RobotController()
r.connect()

r.left(125)
r.forward(350)

# go left into room at marker and rescue person
if True:
    r.left(640)
    r.forward(0)

    # add person rescue here

    r.backward(0)
    r.right(640)

    r.backward(350)
    r.right(40)
    r.left(40)
    r.forward(350)


r.forward(600)

# go into room and extinguish fire
if True:
    r.left(600)
    r.forward(30)

    # add fire extinguishing here

    r.backward(30)
    r.right(600)


r.forward(400)
r.rotate_counterclockwise(86)
r.forward(1600)

# go into room and take temperature
if True:
    r.left(75)

    # add temperature taking here

    r.right(75)


r.forward(520)
r.left(750)
r.backward(750)
r.rotate_counterclockwise(90)
r.forward(800)

# go into room and extinguish fire
# add marker check here
if True:
    r.right(80)
    r.forward(400)
    r.left(500)

    # add extinguishing here

    r.right(500)
    r.backward(400)
    r.left(50)


r.left(1000)
r.forward(200)
r.left(450)

# go into room and rescue person
# add marker check here
if True:
    r.right(50)
    r.forward(300)
    r.left(350)

    # add rescue code here

    r.right(350)
    r.backward(300)
    r.left(50)


# return to the entrance
r.backward(100)
r.right(1500)
r.backward(800)
r.right(700)
r.backward(900)
r.left(2200)
r.forward(1400)

# plot the graph
