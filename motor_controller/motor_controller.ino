/*
*   Upload the following to your arduino board.
*      To start run 
*        roslaunch motor_controller.launch
*        rosrun serial_arduino serial_node.py /dev/ttyUSB0 (has to fix an import error in rosserial_python to make it work)
*/

#include <ros.h>
#include <std_msgs/Empty.h>
#include "SentryMotorController.h"

ros::NodeHandle node_handle;

int pwm_pin_tilt = 1;
int direction_pin_tilt = 2; 
int pwm_pin_pan = 3;
int direction_pin_pan = 4;

int step_speed_tilt = 100;
int step_speed_pan = 100;


SentryMotorController tilt_motor(step_speed_tilt, pwm_pin_tilt, direction_pin_tilt);
SentryMotorController pan_motor(step_speed_pan, pwm_pin_pan, direction_pin_pan);

void go_up_callback(const std_msgs::Empty& empty_msg)
  {
    node_handle.loginfo("going up");
    tilt_motor.spin_cw();
  }

void go_down_callback(const std_msgs::Empty& empty_msg) 
  {
    node_handle.loginfo("going down");
    tilt_motor.spin_ccw();
  }

void go_left_callback(const std_msgs::Empty& empty_msg)
  {
    node_handle.loginfo("going left");
    pan_motor.spin_cw();
  }

void go_right_callback(const std_msgs::Empty& empty_msg)
  {
    node_handle.loginfo("going right");
    pan_motor.spin_ccw();
  }
  
void stop_tilt_callback(const std_msgs::Empty& empty_msg)  
  {
    node_handle.loginfo("stopping tilt");
    tilt_motor.stop();
  }
  
void stop_pan_callback(const std_msgs::Empty& empty_msg)  
  {
    node_handle.loginfo("stopping pan");
    pan_motor.stop();
  }


ros::Subscriber<std_msgs::Empty> go_up_sub("go_up", &go_up_callback );
ros::Subscriber<std_msgs::Empty> go_down_sub("go_down", &go_down_callback);
ros::Subscriber<std_msgs::Empty> go_right_sub("go_left", &go_left_callback);
ros::Subscriber<std_msgs::Empty> go_left_sub("go_right", &go_right_callback);
ros::Subscriber<std_msgs::Empty> stop_tilt_sub("stop_tilt", &stop_tilt_callback);
ros::Subscriber<std_msgs::Empty> stop_pan_sub("stop_pan", &stop_pan_callback);

void setup()
  { 
    node_handle.initNode();
    node_handle.subscribe(go_up_sub);
    node_handle.subscribe(go_down_sub);
    node_handle.subscribe(go_right_sub);
    node_handle.subscribe(go_left_sub);
    node_handle.subscribe(stop_tilt_sub);
    node_handle.subscribe(stop_pan_sub);
  }

void loop()
  {  
    node_handle.spinOnce();
    delay(1);
  }
