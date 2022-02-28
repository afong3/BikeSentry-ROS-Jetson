#include <ros.h>
#include <std_msgs/Empty.h>
#include "SentryMotorController.h"

int pwm_pin_up_down = 1;
int direction_pin_up_down = 2; 
int pwm_pin_left_right = 3;
int direction_pin_left_right = 4;

int step_speed_up_down = 100;
int step_speed_left_right = 100;


SentryMotorController up_down_motor(step_speed_up_down, pwm_pin_up_down, direction_pin_up_down);
SentryMotorController left_right_motor(step_speed_left_right, pwm_pin_left_right, direction_pin_left_right);

void go_up_callback(const std_msgs::Empty& empty_msg)
  {
    up_down_motor.spin_cw();
  }

void go_down_callback(const std_msgs::Empty& empty_msg) 
  {
    up_down_motor.spin_ccw();
  }

void go_left_callback(const std_msgs::Empty& empty_msg)
  {
    left_right_motor.spin_cw();
  }

void go_right_callback(const std_msgs::Empty& empty_msg)
  {
    left_right_motor.spin_ccw();
  }
  
void stop_up_down_callback(const std_msgs::Empty& empty_msg)  
  {
    up_down_motor.stop();
  }
  
void stop_left_right_callback(const std_msgs::Empty& empty_msg)  
  {
    left_right_motor.stop();
  }

ros::NodeHandle node_handle;
ros::Subscriber<std_msgs::Empty> go_up_sub("go_up", &go_up_callback );
ros::Subscriber<std_msgs::Empty> go_down_sub("go_down", &go_down_callback);
ros::Subscriber<std_msgs::Empty> go_right_sub("go_left", &go_left_callback);
ros::Subscriber<std_msgs::Empty> go_left_sub("go_right", &go_right_callback);
ros::Subscriber<std_msgs::Empty> stop_up_down_sub("go_right", &stop_up_down_callback);
ros::Subscriber<std_msgs::Empty> stop_left_right_sub("go_right", &stop_left_right_callback);

void setup()
{ 
  node_handle.initNode();
  node_handle.subscribe(go_up_sub);
  node_handle.subscribe(go_down_sub);
  node_handle.subscribe(go_right_sub);
  node_handle.subscribe(go_left_sub);
  node_handle.subscribe(stop_up_down_sub);
  node_handle.subscribe(stop_left_right_sub);
}

void loop()
{  
  node_handle.spinOnce();
  delay(1);
}
