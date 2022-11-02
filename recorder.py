import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Pose


output = open('output.csv', 'wb', 0)

def callback(data: ModelStates):
    index = data.name.index("robot")
    pose: Pose = data.pose[index]
    output.write(f"{pose.position.x},{pose.position.y}\n".encode('ascii'))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/gazebo/model_states", ModelStates, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
