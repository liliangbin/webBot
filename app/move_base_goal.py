import time

import rospy
from geometry_msgs.msg import PoseStamped


class RosGoal(object):
    def __init__(self):
        self.goal = None
        pass

    def pub(self, pose_stamp):
        rospy.init_node('local_move_base_goal')
        pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)
        time.sleep(1)
        # waiting for subscribers connected with publisher it cos a little time
        # reference https://answers.ros.org/question/306582/unable-to-publish-posestamped-message/
        # more message  ,baidu ,rubbish  garbage
        try:
            pub.publish(pose_stamp)
            print('publish')
            return 'done'
        except Exception:
            print('exception')

    def publish_goal(self, pose_to_location, frame_id='map'):
        self.goal = PoseStamped()
        self.goal.pose.position.x = pose_to_location.position_x
        self.goal.pose.position.y = pose_to_location.position_y
        self.goal.pose.position.z = pose_to_location.position_z
        self.goal.pose.orientation.x = pose_to_location.orientation_x
        self.goal.pose.orientation.y = pose_to_location.orientation_y
        self.goal.pose.orientation.z = pose_to_location.orientation_z
        self.goal.pose.orientation.w = pose_to_location.orientation_w
        self.goal.header.seq = 1
        self.goal.header.stamp = rospy.Time.now()
        self.goal.header.frame_id = frame_id

        self.pub(self.goal)


if __name__ == '__main__':
    pose = PoseStamped()
    pose.pose.position.x = 0.7
    pose.pose.orientation.z = 0.4
    ros_goal = RosGoal()
    ros_goal.publish_goal(pose_stamp=pose)
