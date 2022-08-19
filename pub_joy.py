import rclpy
from rclpy.node import Node
from std_msgs.msg import string   #import string message from the standard messages ROS library
from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import pygame
from pygame.locals import *

def print_add(joy):
    print('Added', joy)
def print_remove(joy):
    print('Removed', joy)

#     if key.value == Key.HAT_UP:
#         print("up")
# def key_received(key):
#     print('received', key)
#     if key.value == Key.HAT_UP:
#         # move_up()
#     elif key.value == Key.HAT_RIGHT:
#         # move_right()
#     if key.value == Key.HAT_LEFT:
#        # move_left()
#     elif key.value == Key.HAT_DOWN:
#         move_down()
#     if key.value == Key.BUTTON:
#         # move_back()



# def msg_by_joy():


# the ROS client library contains a node class with all the different ROS functionality to implement in our code so creat
# own class which inherits the functionality of the node class.

class joy_pubob(Node):
	def __init__(self):
		super().__init__("!!!!!STsART_JOYSTICK!!!!!") #super function to gain access to the 'init' method from our node object

                                                        # START JOYSTICK is node name.
                                                        # now our node is initialized.
        #create our publisher, create class member varial 'pub' and set it = to 'self.create publisher' function which we
        #inherites when we initialized the node above, 'the create publisher' function take three arguments 1st ROS MESSAGES 
        #2nd topic name , 3rd argument 	QoS profile size, Qos stands for quality of service. just like queue 
 
       
		self.pub= self.create_publisher(string, key,10)    
		self.timer = self.create_timer(2, self.publish_joy_key)     #it takes two parameters, 1st rate of our timere in sec and the callback function we want to run at that rate.
       
    def publish_joy_key(self): 
    	msg = string() #create message object we want to load with the data.
    	msg.data = Key
    	self.pub.publish(msg)
    # def key_received(key):
    # 	KEY = print('received', key)

def main():  #initialize our ros DDS communication.
	rclpy.init()   #Inititalization is done by calling init() for a particular Context. This must be done before any ROS nodes can be created.
    my_pub = joy_pubob()

    print("publisher is running..........")



   # run_event_loop(print_add, print_remove, key_received)

    try:
    	rclpy.spin(my_pub)

    except KeyboardInterrupt:
    	my_pub.destory_node()
    	rclpy.shutdown()


if __name__ == '__main__':
	main()
