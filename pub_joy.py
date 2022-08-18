import rclpy
from rclpy.node import Node




# the ROS client library contains a node class with all the different ROS functionality to implement in our code so creat
# own class which inherits the functionality of the node class.

class joy_pubob(Node):
	def __init__(self):
		super().__init__("!!!!!STsART_JOYSTICK!!!!!")     #super function to gain access to the 'init' method from our node object

                                                        # START JOYSTICK is node name.





def main():  #initialize our ros DDS communication.
	rclpy.init()   #Inititalization is done by calling init() for a particular Context. This must be done before any ROS nodes can be created.


if __name__ == '__main__':
	main()