import robot
from matplotlib import pyplot as plt

xs = []
ys = []
room_num = 0

r = robot.RobotController()
r.connect()

xs.append(room_num)
ys.append(r.take_temperature())
room_num += 1

r.left(125)
r.forward(350)

# go left into room at marker and rescue person
if r.read_marker() == 1:
    r.left(640)
    r.forward(50)

    if r.scan_for_people():
        r.rescue_person()

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.backward(50)
    r.right(640)

    r.backward(350)
    r.right(50)
    r.left(50)
    r.forward(350)


r.forward(600)

# go into room and extinguish fire
if r.read_marker() == 1:
    r.left(600)
    r.forward(75)

    while r.scan_for_fire():
        r.extinguish_fire()

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.backward(75)
    r.right(600)


r.forward(400)
r.rotate_counterclockwise(86)
r.forward(1600)

# go into room and take temperature
if r.read_marker() == 1:
    r.left(75)

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.right(75)


r.forward(550)
r.left(750)
r.backward(750)
r.rotate_counterclockwise(90)
r.forward(800)

# go into room and extinguish fire
if r.read_marker() == 1:
    r.right(50)
    r.forward(400)
    r.left(600)

    while r.scan_for_fire():
        r.extinguish_fire()

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.right(600)
    r.backward(400)
    r.left(50)


r.left(1000)
r.forward(200)
r.left(450)

# go into room and rescue person
if r.read_marker() == 1:
    r.right(50)
    r.forward(300)
    r.left(350)

    if r.scan_for_people():
        r.rescue_person()

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

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

plt.plot(xs, ys, 'ro')
plt.xlabel('Room Number')
plt.ylabel('Room Temperature')
plt.show()
