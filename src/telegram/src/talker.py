#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

v_mtr = 12.6
v_pc = 12.5
t_est_mtr = 33.3
t_est_pc = 50.32
trash_level = 10.0

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
