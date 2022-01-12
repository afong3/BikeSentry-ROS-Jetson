# This library will manage data from the camera
# Purpose: Receives data from the Camera and outputs instructions for pan and tilt motors
# Python2.7
# Refer to Confluence directory: StopBikeTheft/Designs/ROS Design/CameraDataManager

def calc_image_center(dim_x: float, dim_y:float):
	"""
	Description: Finds center x & y pixels of the defined image size 
		     stores the image center as properties.
	Returns: void
	"""
	
	pass

def create_motor_instructions_pan(pixels_x):
	"""
	Description: Creates the pan motor instruction
	Returns: void
	"""
	pan_instruction = enum("left","right", "none")

	pass

def create_motor_instructions_tilt(pixels_y):
	"""
	Description: Creates the tilt motor instructions
	Returns: void 
	"""

	pass
