cmake_minimum_required(VERSION 2.8.3)
project(visualize_euler)

find_package(
  catkin REQUIRED COMPONENTS
  roscpp  
  rospy
  sensor_msgs
  dynamic_reconfigure
)


generate_dynamic_reconfigure_options(
  cfg/EulerAngles.cfg
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy sensor_msgs dynamic_reconfigure
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(visualize_euler_node 
  src/visualize_euler_node.cpp
)

add_dependencies(
  visualize_euler_node 
  ${PROJECT_NAME}_gencfg
)

target_link_libraries(visualize_euler_node
  ${catkin_LIBRARIES}
)

add_dependencies(visualize_euler_node 
  ${visualize_euler_EXPORTED_TARGETS} 
  ${catkin_EXPORTED_TARGETS}
)

