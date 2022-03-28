/*
    Controls a single wheel Motor . TO contorl just need a high to a given pin
    The A wheel motor either propels the ball when shooting, or loads the balls by spinning ball loader motor.
*/

#include "WheelMotorController.h"

WheelMotorController::WheelMotorController(int speed, int enable_a_pin, int in_1_pin, int in_2_pin) 
  { 
    this->speed = speed;
    this->enable_a_pin = enable_a_pin;
    this->in_1_pin = in_1_pin;
    this->in_2_pin = in_2_pin; 
    this->init_motor_pins();
  } 
void WheelMotorController::init_motor_pins()
  {
    pinMode(this->enable_a_pin, OUTPUT);
    pinMode(this->in_1_pin, OUTPUT);
    pinMode(this->in_2_pin, OUTPUT);
  }

void WheelMotorController::start_spin()
  {
    // Write the logic to start spining a motor
    digitalWrite(this->in_1_pin, HIGH);
    digitalWrite(this->in_2_pin, LOW);
    analogWrite(this->enable_a_pin, this->speed);
  }

void WheelMotorController::stop_spin()
  {
    // Write the logic to stop spining a motor
    analogWrite(this->enable_a_pin, 0);
  }