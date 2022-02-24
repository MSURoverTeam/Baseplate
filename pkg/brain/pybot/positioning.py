import rospy
from nav_msgs.msg import Odometry
from tf.transformations import *

from pybot.communication import chain_callbacks


def quaternion_to_theta(quaternion, circle=True):
    t1 = +2.0 * (quaternion.w * quaternion.z + quaternion.x * quaternion.y)
    t2 = +1.0 - 2.0 * (quaternion.y ** 2 + quaternion.z ** 2)
    degs = math.degrees(math.atan2(t1, t2))

    if circle and degs < 0:
        degs = 360 + degs
    return degs


def quaternion_msg_to_euler(quaternion_message):
    return euler_from_quaternion ([orientation.x, orientation.y, orientation.z, orientation.w])  # (roll, pitch, yaw)


def info_callback(msg):
    orientation = msg.pose.pose.orientation
    position = msg.pose.pose.position
    rospy.loginfo(
        "Theta: {theta};".format(theta=quaternion_to_theta(orientation)) + " " +
        "Position: {pos}".format(pos=str(position).replace('\n', ', '))
    )


def subscribe_to_odometry(callbacks, *args, **kwargs):
    return rospy.Subscriber('odom', Odometry, chain_callbacks(callbacks), **kwargs)
