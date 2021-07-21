import robot
import matplotlib.pyplot as plt

r = robot.RobotController()
r.connect()

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
# insert marker check here
if r.read_marker() == 1:
    r.left(640)

    if r.scan_for_people():
        r.rescue_person()

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.right(640)

    r.backward(350)
    r.right(40)
    r.left(40)
    r.forward(350)


r.forward(600)

# insert marker check here
if r.read_marker() == 1:
    r.left(600)
    r.forward(30)

    while r.scan_for_fire():
        r.extinguish_fire()

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.backward(30)
    r.right(600)


r.forward(400)
r.rotate_counterclockwise(86)
r.forward(1600)

# go into room and take temperature
# insert marker check here
if r.read_marker() == 1:
    r.left(75)

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.right(75)


r.forward(520)
r.left(750)
r.backward(750)
r.rotate_counterclockwise(90)
r.forward(900)

# add marker check here
if r.read_marker() == 1:
    r.right(80)
    r.forward(300)
    r.left(550)

    while r.scan_for_fire():
        r.extinguish_fire()

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.right(550)
    r.backward(300)
    r.left(80)


r.left(1400)
r.forward(100)

# go into room and rescue person
# add marker check here
if r.read_marker() == 1:
    r.right(100)
    r.forward(300)
    r.left(400)

    if r.scan_for_people():
        r.rescue_person()

    xs.append(room_num)
    ys.append(r.take_temperature())
    room_num += 1

    r.right(400)
    r.backward(300)
    r.left(100)


# return to the entrance
r.backward(100)
r.right(1500)
r.backward(800)
r.right(700)
r.backward(900)
r.left(2200)
r.forward(1350)

plt.plot(xs, ys, 'ro')
plt.title('Temperature for the maze')
plt.xlabel('Room Number')
plt.ylabel('Room Temperature')
plt.grid(True)
plt.show()
