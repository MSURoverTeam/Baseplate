import math
import time

import rospy
from geometry_msgs.msg import Twist, Vector3

from pybot.executors import Action

hz = 20
one_rate = rospy.Rate(hz)

full_circle = 2*math.pi  # rad

start = time.time()
duration = 5

forward = Twist(linear=Vector3(x=0.05))


def conv(speed):
    return speed * 1.2


turn_speed = 1.0
clockwise = Twist(angular=Vector3(z=conv(turn_speed)))
rotation_time = full_circle / 2.0 / turn_speed


class MovingAction(Action):
    def __init__(self, *args, **kwargs):
        self.mover = kwargs.pop('mover')
        super(MovingAction, self).__init__(*args, **kwargs)


class Forward(MovingAction):
    condition = lambda self: (time.time() - self.start) < duration
    rate = one_rate

    def do(self):
        self.mover.publish(forward)


class Turn(MovingAction):
    condition = lambda self: (time.time() - self.start) <= rotation_time
    rate = one_rate

    def do(self):
        self.mover.publish(clockwise)


class Circle(MovingAction):
    rate = one_rate

    def do(self):
        speed = 0.15
        diameter = 0.5

        radius = diameter / 2
        okr = 2.0 * math.pi * radius
        fraction = 1.0 / hz
        parts = okr / speed
        turn = full_circle / parts

        self.mover.publish(Twist(
            linear=Vector3(x=speed),
            angular=Vector3(z=turn)
        ))
