#include "ros/ros.h"
#include "std_msgs/String.h"

/*
#include "serial/serial.h"

serial::Serial ser;

void write_callback(const std_msgs::String::ConstPtr& msg){
  ROS_INFO_STREAM("Writing to serial port" << msg->data);
  ser.write(msg->data);
}
*/
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "slave1_subscriber");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("chatter", 1000, chatterCallback);

  ros::spin();

  return 0;
}
