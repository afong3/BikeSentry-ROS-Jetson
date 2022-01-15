# This library will manage data from the camera
# Purpose: Receives data from the Camera and outputs instructions for pan and tilt motors
# Python2.7
# Refer to Confluence directory: StopBikeTheft/Designs/ROS Design/CameraDataManager

class CameraDataManager:
	
	def __init__(self, image_width, image_height):
		
		self.width = image_width
		self.height = image_height
		self.center = self.calc_image_center(image_width, image_height)

	def calc_image_center(self, dim_x: float, dim_y:float):
		"""
		Description: Finds center x & y pixels of the defined image size 
				stores the image center as properties.
		Returns: void
		"""
		
		pass

	def create_motor_instructions_pan(self, pixels_x):
		"""
		Description: Creates the pan motor instruction
		Returns: void
		"""
		left_instruction = "left"
		left_instruction = "right"
		none_instruciton = "none"

		pass

	def create_motor_instructions_tilt(self, pixels_y):
		"""
		Description: Creates the tilt motor instructions
		Returns: void 
		"""

		pass
