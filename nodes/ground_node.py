import rospy
import CFData
import CFImage
import CFCommand
import CFMotion



class GroundStation:

    # receiving flow object for use by Ground station
    class CF_RX:
        def __init__(self, ID, cf_node):
            self.id = ID
            self.cf_node = cf_node

            #need to facilitate a set of subscribers and publishers per cf node

            self.data_sub = rospy.Subscriber('cf/%d/data'%self._id, CFData, data_cb)
            self.image_sub = rospy.Subscriber('cf/%d/image'%self._id, CFImage, image_cb)

            self.cmd_pub = rospy.Publisher('cf/%d/command'%self._id, CFCommand, queue_size=10)
            self.motion_pub = rospy.Publisher('cf/%d/motion'%self._id, CFMotion, queue_size=10)


    def __init__(self):
        #dictionary from ID to RXObject
        self.cf_nodes = {}

    ## CALLBACKS ##

    def image_cb(self, msg):
        pass

    def data_cb(self, msg):
        pass

    ## SETTERS ##

    def add_cf_node(self, id, uri):
        # spawn new CF Node through this method
        # instead of creating one first and then connecting
        pass

    ## IMAGE HANDLING ##

    # TODO: add RL (~_~)

    ## THREADS
    def loop(self):
        pass




if __name__ == '__main__':
    rospy.init_node('GroundNode', anonymous=True)
    cf = GroundStation()

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.spinOnce()
        rate.sleep()
