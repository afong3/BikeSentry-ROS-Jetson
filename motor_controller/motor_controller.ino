/*
*   Upload the following to your arduino board.
*      To start run 
*        roslaunch motor_controller.launch
*        rosrun serial_arduino serial_node.py /dev/ttyUSB0 (has to fix an import error in rosserial_python to make it work)
*/

#include <ros.h>
#include <std_msgs/Empty.h>
#include "SentryMotorController.h"
#include "WheelMotorController.h"
#include <Servo.h>
#include <std_msgs/Float64.h>

ros::NodeHandle node_handle;

int pwm_pin_tilt = 6;
int direction_pin_tilt = 7; 
int tilt_enable_pin = 8;
int pwm_pin_pan = 10;
int direction_pin_pan = 11;
int pan_enable_pin = 12;

int step_speed_tilt = 100;
int step_speed_pan = 100;

int flywheels_speed = 255;
int flywheels_enable_a_pin = 5; 
int flywheels_in_1_pin = 4;
int flywheels_in_2_pin = 3;

int servo_pin = 13;
int pos_high = 180;
int pos_low = 120;

float MESSAGE_FLOAT = 0.0;

SentryMotorController tilt_motor(step_speed_tilt, pwm_pin_tilt, direction_pin_tilt, tilt_enable_pin);
SentryMotorController pan_motor(step_speed_pan, pwm_pin_pan, direction_pin_pan, pan_enable_pin);
WheelMotorController flywheels(flywheels_speed, flywheels_enable_a_pin, flywheels_in_1_pin, flywheels_in_2_pin);
Servo servo_ball_loader;
std_msgs::Empty GLOBAL_EMPTY_MSG;
std_msgs::Float64 fl;
ros::Publisher done_shot_pub("done_shot", &fl);

void go_up_callback(const std_msgs::Empty& empty_msg)
  {
    node_handle.loginfo("go up");
    tilt_motor.spin_ccw();
  }

void go_down_callback(const std_msgs::Empty& empty_msg) 
  {
    node_handle.loginfo("go down");
    tilt_motor.spin_cw();
  }

void go_left_callback(const std_msgs::Empty& empty_msg)
  {
    node_handle.loginfo("go left");
    pan_motor.spin_ccw();
  }

void go_right_callback(const std_msgs::Empty& empty_msg)
  {
    node_handle.loginfo("go right");
    pan_motor.spin_cw();
  }
  
void stop_tilt_callback(const std_msgs::Empty& empty_msg)  
  {
    node_handle.loginfo("stop tilt");
    tilt_motor.disable_motor();
  }
  
void stop_pan_callback(const std_msgs::Empty& empty_msg)  
  {
    node_handle.loginfo("stop pan");
    pan_motor.disable_motor();
  }

void start_flywheel_callback(const std_msgs::Empty& empty_msg)  
  {
    node_handle.loginfo("start flywheel");
    flywheels.start_spin();
  }

void stop_flywheel_callback(const std_msgs::Empty& empty_msg)  
  {
    node_handle.loginfo("stop flywheel");
    flywheels.stop_spin();
  }

void servo_shoot_callback(const std_msgs::Empty& empty_msg)
  {
    node_handle.loginfo("servo shooting");
    fl.data = MESSAGE_FLOAT;
    /*In here add some code to shoot one ball! Hopefully this works. Good luck Adam!*/
    servo_ball_loader.write(pos_high);
    delay(500);
    servo_ball_loader.write(pos_low);
    delay(500);
    done_shot_pub.publish(&fl);
  }

ros::Subscriber<std_msgs::Empty> go_up_sub("go_up", &go_up_callback );
ros::Subscriber<std_msgs::Empty> go_down_sub("go_down", &go_down_callback);
ros::Subscriber<std_msgs::Empty> go_right_sub("go_left", &go_left_callback);
ros::Subscriber<std_msgs::Empty> go_left_sub("go_right", &go_right_callback);
ros::Subscriber<std_msgs::Empty> stop_tilt_sub("stop_tilt", &stop_tilt_callback);
ros::Subscriber<std_msgs::Empty> stop_pan_sub("stop_pan", &stop_pan_callback);
ros::Subscriber<std_msgs::Empty> start_flywheel_spin_sub("start_flywheel", &start_flywheel_callback);
ros::Subscriber<std_msgs::Empty> stop_flywheel_spin_sub("stop_flywheel", &stop_flywheel_callback);
ros::Subscriber<std_msgs::Empty> servo_shoot_sub("servo_shoot", &servo_shoot_callback);


void setup()
  { 
    servo_ball_loader.attach(servo_pin);
    servo_ball_loader.write(pos_low);
    pinMode(pwm_pin_tilt, OUTPUT);
    pinMode(direction_pin_tilt, OUTPUT);
    pinMode(pwm_pin_pan, OUTPUT);
    pinMode(direction_pin_pan, OUTPUT);
    pinMode(tilt_enable_pin, OUTPUT);
    pinMode(pan_enable_pin, OUTPUT);
    
    node_handle.initNode();
    node_handle.subscribe(go_up_sub);
    node_handle.subscribe(go_down_sub);
    node_handle.subscribe(go_right_sub);
    node_handle.subscribe(go_left_sub);
    node_handle.subscribe(stop_tilt_sub);
    node_handle.subscribe(stop_pan_sub);
    node_handle.subscribe(start_flywheel_spin_sub);
    node_handle.subscribe(stop_flywheel_spin_sub);
    node_handle.subscribe(servo_shoot_sub);
    node_handle.advertise(done_shot_pub);
  }

void loop()
  {  
    node_handle.spinOnce();
    delay(1);
  }
