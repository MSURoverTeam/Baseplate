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


def do():
    print("Publishing turn")
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        for p in FRONT_PUB:
            p.publish(Float64(data=1.5))
        for p in BACK_PUB:
            p.publish(Float64(data=0.4))
        rate.sleep()

