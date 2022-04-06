cmake_minimum_required(VERSION 3.0.2)
project(brain)

add_compile_options(-std=c++14)

find_package(catkin REQUIRED COMPONENTS
  message_runtime
  rospy
  std_msgs
)

find_package(gazebo REQUIRED)

catkin_python_setup()

catkin_package(
  LIBRARIES brain
  CATKIN_DEPENDS std_msgs message_runtime
  DEPENDS gazebo_ros
)

catkin_install_python(
  PROGRAMS bin/control
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
