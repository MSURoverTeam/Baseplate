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

add_message_files(
  FILES
  ServoCommand.msg
)

##add_service_files(
##  FILES
##  GetEvent.srv
##)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  LIBRARIES brain
  CATKIN_DEPENDS std_msgs roscpp message_runtime
  DEPENDS gazebo_ros
)

catkin_install_python(
  PROGRAMS bin/pybot
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

include_directories(include ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS} ${SDFormat_INCLUDE_DIRS})

add_executable(ouroboros_pub src/ouroboros_pub.cpp)
add_dependencies(ouroboros_pub ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ouroboros_pub ${catkin_LIBRARIES})

add_executable(ouroboros_sub src/ouroboros_sub.cpp)
add_dependencies(ouroboros_sub ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ouroboros_sub ${catkin_LIBRARIES})
