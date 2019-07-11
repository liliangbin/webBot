import rospy
from geometry_msgs.msg import PoseStamped


def send_move_base_goal(posetolocation):
    # rostopic
    # pub / move_base_simple / goal
    # geometry_msgs / PoseStamped \ '{header: {frame_id: "map"},pose: {position:{x: 0.0,y: 0,z: 0},orientation: {x: 0,y: 0,z: 0,w: 1}}}'
    #
    # rospy.Publisher
    pass
