# This library will manage data from the camera
# Purpose: Receives data from the Camera and outputs instructions for pan and tilt motors
# Python2.7
# Refer to Confluence directory: StopBikeTheft/Designs/ROS Design/CameraDataManager


class CameraDataManager:

		# Offset from the center point to create the target point. 
		# AKA where the camera wants to center itself on in relation to the detected person.
    # Positive values mean up and right, negative values mean down and left.
    _X_OFFSET = 0
    _Y_OFFSET = 0

    def __init__(self, image_width, image_height):
        self.target_x, self.target_y = self.where_to_aim(image_width, image_height)
        self.set_stop_zone()

    def where_to_aim(self, dim_x, dim_y):
        center_x, center_y = self.calc_image_center(dim_x, dim_y)
        target_x = center_x + CameraDataManager._X_OFFSET
        target_y = center_y + CameraDataManager._Y_OFFSET
        return (target_x, target_y)

    def calc_image_center(self, dim_x, dim_y):
        """
        Description: Finds center x & y pixels of the defined image size
                        stores the image center as properties.
        Returns: (x,y)
        """
        center_x = dim_x / 2
        center_y = dim_y / 2

        return (center_x, center_y)

    def set_stop_zone(self):
        """
        Inside of the stop zone the motors will be told to stop moving.
        It will be assumed that a person is inside the frame.
        """
        stop_zone_width = 350
        stop_zone_height = 720

        self.stop_zone_low_x = self.target_x - stop_zone_width / 2
        self.stop_zone_high_x = self.target_x + stop_zone_width / 2

        self.stop_zone_low_y = self.target_y - stop_zone_height / 2
        self.stop_zone_high_y = self.target_y + stop_zone_height / 2

    def create_motor_instructions_pan(self, pixels_x):
        """
        Description: Creates the pan motor instruction
        Returns: "left" or "right"
        """
        if pixels_x < self.stop_zone_low_x:
            pan_instruction = "left"
        elif pixels_x > self.stop_zone_high_x:
            pan_instruction = "right"
        else:
            pan_instruction = "stop_pan"

        return pan_instruction

    def create_motor_instructions_tilt(self, pixels_y):
        """
        Description: Creates the tilt motor instructions
        Returns: "up" or "down"
        """
        if pixels_y < self.stop_zone_low_y:
            tilt_instruction = "down"
        elif pixels_y > self.stop_zone_high_y:
            tilt_instruction = "up"
        else:
            tilt_instruction = "stop_tilt"

        return tilt_instruction
