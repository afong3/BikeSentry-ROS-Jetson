# Purpose: Receives a pan/tilt instruction and executes
# Python2.7
# Refer to StopBikeTheft/Designs/Ros Design/MotorManager


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


