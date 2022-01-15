# This library will manage data from the camera
# Purpose: Receives data from the Camera and outputs instructions for pan and tilt motors
# Python2.7
# Refer to Confluence directory: StopBikeTheft/Designs/ROS Design/CameraDataManager

class CameraDataManager:
	
	def __init__(self, image_width, image_height):
		
		self.width = image_width
		self.height = image_height
		self.center_x, self.center_y = self.calc_image_center(image_width, image_height)

	def calc_image_center(self, dim_x: float, dim_y:float):
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
			tilt_instruction = "<-"
		elif pixels_x > self.center_y:
			tilt_instruction = "->"
		
		return tilt_instruction


	def create_motor_instructions_tilt(self, pixels_y):
		"""
		Description: Creates the tilt motor instructions
		Returns: "up" or "down" 
		"""
		if pixels_y < self.center_y:
			tilt_instruction = "down"
		elif pixels_y > self.center_y:
			tilt_instruction = "up"
		
		return tilt_instruction
