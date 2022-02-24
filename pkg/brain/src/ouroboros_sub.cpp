#include "ros/ros.h"
#include "std_msgs/String.h"

void msgCallback(const std_msgs::StringConstPtr& msg)
{
    ROS_INFO("recieve msg = %s", msg->data.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "ouroboros_sub");
    ROS_INFO("SUBSCRIBER is up");
    ros::NodeHandle nh;

    ros::Subscriber ouroboros_sub = nh.subscribe("chatter", 100, msgCallback);

    ros::spin();
    return 0;
}
