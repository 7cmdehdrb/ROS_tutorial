#!/usr/bin/python

import rospy
from random import randint
from std_msgs.msg import Int64


if __name__ == '__main__':
    rospy.init_node("publisher_test")

    publisher = rospy.Publisher(
        name="simple_pub", data_class=Int64, queue_size=1)

    r = rospy.Rate(1)
    while not rospy.is_shutdown():

        msg = Int64()
        msg.data = randint(0, 255)

        rospy.loginfo(msg)

        publisher.publish(msg)

        r.sleep()
