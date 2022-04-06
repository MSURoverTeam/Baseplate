import rospy

from control.lifecycle import setup_finalizers
from control.communication import launch_spinner_thread


def setup_listeners():
    # TODO: subscribers, chain_callbacks
    return launch_spinner_thread()


def run():
    import control.program as program

    rospy.init_node('brain')
    rospy.loginfo("Starting <brain> node")

    setup_finalizers({})
    #spinner = setup_listeners()  # After all else is done - spinner.join()

    program.do()


if __name__ == "__main__":
    run()
