#include "ros/ros.h"
#include "std_msgs/String.h"


int main(int argc, char **argv)
{
    ros::init(argc, argv, "ouroboros_pub");
    ROS_INFO("PUBLISHER is up");
    ros::NodeHandle nh;

    ros::Publisher ouroboros_pub = nh.advertise<std_msgs::String>("chatter", 1000);
    ros::Rate loop_rate(10);

    int count = 0;
    while (ros::ok())
    {
        std_msgs::String msg;

        std::string message_data = "Message " + std::to_string(count);
        msg.data = message_data;

        ROS_INFO("%s", msg.data.c_str());

        ouroboros_pub.publish(msg);

        loop_rate.sleep();
        ++count;
    }

    return 0;
}
