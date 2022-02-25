cmake_minimum_required(VERSION 3.0.2)
project(brain)

add_compile_options(-std=c++14)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  message_runtime
  roscpp
  rospy
  std_msgs
)

find_package(gazebo REQUIRED)

catkin_python_setup()

catkin_package(
  LIBRARIES brain
  CATKIN_DEPENDS std_msgs roscpp message_runtime
  DEPENDS gazebo_ros
)

include_directories(include ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS} ${SDFormat_INCLUDE_DIRS})
