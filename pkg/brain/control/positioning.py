import rospy
from nav_msgs.msg import Odometry
from tf.transformations import *

from control.communication import chain_callbacks


def quaternion_to_theta(quaternion, circle=True):
    t1 = +2.0 * (quaternion.w * quaternion.z + quaternion.x * quaternion.y)
    t2 = +1.0 - 2.0 * (quaternion.y ** 2 + quaternion.z ** 2)
    degs = math.degrees(math.atan2(t1, t2))

    if circle and degs < 0:
        degs = 360 + degs
    return degs


# (roll, pitch, yaw)
def quaternion_msg_to_euler(quaternion_message):
    return euler_from_quaternion ([
        quaternion_message.x, quaternion_message.y, quaternion_message.z, quaternion_message.w,
    ])


def info_callback(msg):
    orientation = msg.pose.pose.orientation
    position = msg.pose.pose.position
    rospy.loginfo(
        "Theta: {theta};".format(theta=quaternion_to_theta(orientation)) + " " +
        "Position: {pos}".format(pos=str(position).replace('\n', ', '))
    )


def subscribe_to_odometry(callbacks, *args, **kwargs):
    return rospy.Subscriber('odom', Odometry, chain_callbacks(callbacks), **kwargs)
