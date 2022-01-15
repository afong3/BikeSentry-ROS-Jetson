# Purpose: Receives a pan/tilt instruction and executes
# Python2.7
# Refer to StopBikeTheft/Designs/Ros Design/MotorManager


class MotorManager:
	def __init__(self, motor_step_count):
		self.step_count = motor_step_count

	def actuate(self, instruction):
		if(instruction == "right" | instruction == "down"): # Depends on motor orientation
			self.rotate_clockwise(instruction)
		elif(instruction == "left" | instruction == "up"):
			self.rotate_counter_clockwise(instruction)
		else:
			print("no luck")

	def rotate_clockwise(self, instruction):
		if instruction == "up":
			print("^")
		elif instruction == "down":
			print("down")
		elif instruction == "left": 
			

	def rotate_counter_clockwise(self, instruction):
		print("->")


