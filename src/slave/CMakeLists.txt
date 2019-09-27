cmake_minimum_required(VERSION 2.8.3)
project(slave)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  serial
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS
  std_msgs
)

include_directories(${catkin_INCLUDE_DIRS})



add_executable(slave1_subscriber src/slave1_subscriber.cpp)
add_dependencies(slave1_subscriber slave)
target_link_libraries(slave1_subscriber ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} ${OpenCV_LIBS})

add_executable(subscriber src/subscriber.cpp)
add_dependencies(subscriber slave)
target_link_libraries(subscriber ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} ${OpenCV_LIBS})
