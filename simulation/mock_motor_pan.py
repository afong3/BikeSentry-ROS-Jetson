#!/usr/bin/python2.7

import rospy
from std_msgs.msg import Float32

#Hard coding MotorManager version

class MotorManager:
	def __init__(self, motor_step_count):
		self.step_count = motor_step_count

	def actuate(self, instruction):
		if instruction == "right" or instruction == "down": # Depends on motor orientation
			return self.rotate_clockwise(instruction)
		elif instruction == "left" or instruction == "up":
			return self.rotate_counter_clockwise(instruction)
		else:
			return("no luck")

	def rotate_clockwise(self, instruction):
		if instruction == "up":
			return("^")
		elif instruction == "down":
			return("down")
		elif instruction == "left": 
			return("<-")
		elif instruction == "right":
			return("->")

	def rotate_counter_clockwise(self, instruction):
		if instruction == "up":
			return("^")
		elif instruction == "down":
			return("down")
		elif instruction == "left": 
			return("<-")
		elif instruction == "right":
			return("->")




#Hard coding CameraDataManager version 
# This library will manage data from the camera
# Purpose: Receives data from the Camera and outputs instructions for pan and tilt motors
# Python2.7
# Refer to Confluence directory: StopBikeTheft/Designs/ROS Design/CameraDataManager

class CameraDataManager:
	
	def __init__(self, image_width, image_height):
		
		self.width = image_width
		self.height = image_height
		self.center_x, self.center_y = self.calc_image_center(image_width, image_height)

	def calc_image_center(self, dim_x, dim_y):
		"""
		Description: Finds center x & y pixels of the defined image size 
				stores the image center as properties.
		Returns: (x,y)
		"""
		center_x = self.width / 2
		center_y = self.height / 2

		return (center_x, center_y)

	def create_motor_instructions_pan(self, pixels_x):
		"""
		Description: Creates the pan motor instruction
		Returns: "left" or "right"
		"""
		if pixels_x < self.center_y:
			tilt_instruction = "right"
		elif pixels_x > self.center_y:
			tilt_instruction = "left"
		
		return tilt_instruction


	def create_motor_instructions_tilt(self, pixels_y):
		"""
		Description: Creates the tilt motor instructions
		Returns: "up" or "down" 
		"""
		if pixels_y < self.center_y:
			tilt_instruction = "up"
		elif pixels_y > self.center_y:
			tilt_instruction = "down"
		
		return tilt_instruction


STEPS = 0

CameraDataManager = CameraDataManager(1280, 720)
Motor = MotorManager(STEPS)

def listener_x():
    rospy.Subscriber("mock_x_center", Float32, pan_callback)

def pan_callback(pixels_x):

    x = int(pixels_x.data)
    instr = CameraDataManager.create_motor_instructions_pan(x) 

    movement = Motor.actuate(instr)
    rospy.loginfo("x_center: {}   direction:{}".format(x, movement))

def main():
    rospy.init_node("mock_motor_pan")
    listener_x()
    rospy.spin()

if __name__ == "__main__":
    main()