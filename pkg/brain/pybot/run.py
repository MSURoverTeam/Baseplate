import rospy
from geometry_msgs.msg import Twist

from pybot.lifecycle import setup_finalizers
from pybot.executors import execute
from pybot.communication import launch_spinner_thread
from pybot.positioning import info_callback, subscribe_to_odometry


def run():
    rospy.init_node('brain')
    rospy.loginfo("Starting <brain> node")

    import pybot.main as main
    import pybot.stuff as stuff

    mover = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    setup_finalizers({'full_stop': mover})

    subscribe_to_odometry(info_callback)
    stuff.create_service()

    launch_spinner_thread()

    execute(main.Circle(mover=mover))


if __name__ == "__main__":
    run()
