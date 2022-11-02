import math
import rospy
from std_msgs.msg import Float64

from control.executors import execute


LEFT_PUB = [
    rospy.Publisher(f'/rover/wheel_{idx}_position_controller/command', Float64, queue_size=1)
    for idx in range(6, 3, -1)
]

RIGHT_PUB = [
    rospy.Publisher(f'/rover/wheel_{idx}_position_controller/command', Float64, queue_size=1)
    for idx in range(1, 4)
]

BACK_PUB = [LEFT_PUB[-1], RIGHT_PUB[-1]]
FRONT_PUB = [LEFT_PUB[0], RIGHT_PUB[0]]
MID_PUB = [LEFT_PUB[1], RIGHT_PUB[1]]

d = 0.843/2
l1 = 0.330
l2 = 0.232
l3 = 0.097
r1 = math.sqrt(d**2 + (l1 + l2)**2)
r2 = math.sqrt(d**2 + l2**2)
r3 = math.sqrt(d**2 + l3**2)
#r1 = math.sqrt(d**2 + l1**2)
#r2 = d
#r3 = math.sqrt(d**2 + l1**2)
rs = [r1, r2, r3]


def naive_turn(k):
    for p in LEFT_PUB:
        p.publish(Float64(data=-k*r1))
    for p in RIGHT_PUB:
        p.publish(Float64(data=k*r1))


def correct_turn(k):
    RIGHT_PUB[2].publish(k*r3)
    LEFT_PUB[2].publish(-k*r3)

    RIGHT_PUB[1].publish(k*r2)
    LEFT_PUB[1].publish(-k*r2)

    RIGHT_PUB[0].publish(k*r1)
    LEFT_PUB[0].publish(-k*r1)

def correct_move(va, vl):
    for i, wheel in enumerate(LEFT_PUB):
        R = math.sqrt(rs[i]**2 - 2*vl*d/va + (vl**2)/(va**2))
        wheel.publish(R*va)
    for i, wheel in enumerate(RIGHT_PUB):
        R = math.sqrt(rs[i]**2 + 2*vl*d/va + (vl**2)/(va**2))
        wheel.publish(R*va)

def do():
    print("Publishing turn")
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        correct_move(1, 2)
        rate.sleep()
