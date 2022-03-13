# This library will manage data from the camera
# Purpose: Receives data from the Camera and outputs instructions for pan and tilt motors
# Python2.7
# Refer to Confluence directory: StopBikeTheft/Designs/ROS Design/CameraDataManager

class CameraDataManager:
	
	def __init__(self, image_width, image_height):
		
		self.width = image_width
		self.height = image_height
		self.center_x, self.center_y = self.calc_image_center(image_width, image_height)
		self.set_stop_buffer_pan()
		self.set_stop_buffer_tilt()

	def calc_image_center(self, dim_x, dim_y):
		"""
		Description: Finds center x & y pixels of the defined image size 
				stores the image center as properties.
		Returns: (x,y)
		"""
		center_x = self.width / 2
		center_y = self.height / 2

		return (center_x, center_y)
	

	def set_stop_buffer_pan(self):
			"""
				Sets the center box size for what in what range the motors should be stopped
			"""
			center_box_width = 400 

			self.center_box_low_x = self.center_x - center_box_width / 2
			self.center_box_high_x = self.center_x + center_box_width / 2

	def set_stop_buffer_tilt(self):
			"""
				Sets the center box size for what in what range the motors should be stopped
			"""
			center_box_height = 100 

			self.center_box_low_y = self.center_y - center_box_height / 2
			self.center_box_high_y = self.center_y + center_box_height / 2

	def create_motor_instructions_pan(self, pixels_x):
		"""
		Description: Creates the pan motor instruction
		Returns: "left" or "right"
		"""
		if pixels_x < self.center_box_low_x:
			pan_instruction = "left"
		elif pixels_x > self.center_box_high_x:
			pan_instruction = "right"
		else:
			pan_instruction = "stop_pan"

		
		return pan_instruction


	def create_motor_instructions_tilt(self, pixels_y):
		"""
		Description: Creates the tilt motor instructions
		Returns: "up" or "down" 
		"""
		if pixels_y < self.center_box_low_y:
			tilt_instruction = "down"
		elif pixels_y > self.center_box_high_y:
			tilt_instruction = "up"
		else:
			tilt_instruction = "stop_tilt"
		
		return tilt_instruction
