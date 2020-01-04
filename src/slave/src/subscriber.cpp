/* Subscriber string data
 * #include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I read: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "subscriber");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("chatter", 1000, chatterCallback);

  ros::spin();

  return 0;
}
*/

// Subscriber float data
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float64.h"
#include "sensor_msgs/Range.h"
#include "rosserial_arduino/Adc.h"

static double v_motor, v_pc, i_motor,i_pc;
static double level;

void chatterCallback(const sensor_msgs::Range::ConstPtr& range_msg)
{
  level = range_msg->range;
  printf("level:[%.2f]", level);
}

void chatterCallback2(const rosserial_arduino::Adc::ConstPtr& adc_msg)
{
  v_motor = adc_msg->adc0;
  v_pc = adc_msg->adc1;
  i_motor = adc_msg->adc2;
  i_pc = adc_msg->adc3;

  printf("v_motor=[%.2f]->v_pc=[%.2f]->i_mtr=[%.2f]->i_pc=[%.2f]\n",v_motor,v_pc,i_motor,i_pc);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "subscriber");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("ultrasound", 1000, chatterCallback);
  ros::Subscriber sub2 = nh.subscribe("adc_data", 1000, chatterCallback2);

  ros::spin();

  return 0;
}
