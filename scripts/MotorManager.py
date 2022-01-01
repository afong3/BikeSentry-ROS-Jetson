# Purpose: Receives a pan/tilt instruction and executes
# Python2.7
# Refer to StopBikeTheft/Designs/Ros Design/MotorManager


class MotorManager():
	def __init__(self, motor_step_count):
		self.step_count = motor_step_count

	def actuate(self, instruction):
		if("right" | "down"): # Depends on motor orientation
			rotate_clockwise()
		else if("left" | "up"):
			rotate_counter_clockwise()

	def rotate_clockwise(self):
		next

	def rotate_counter_clockwise(self):
		next 


