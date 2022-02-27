#include "SentryMotorController.h"

#define motorInterfaceType 1

SentryMotorController::MotorController(int steps_per_second, int pwm_pin, int direction_pin) 
  {
    this->max_step_speed = 1000;
    this->acceleration = 50;
    this->steps_per_second = steps_per_second; 
    this->pwm_pin = pwm_pin;
    this->direction_pin = direction_pin;
    this->init_motor_pins();
    this->init_motor_settings();
  }

void setMaxSpeed(val)
  {
    this->max_step_speed = val;
  }

void SentryMotorController::setAcceleration(val)
  {
    this->acceleration = val;
  }

void SentryMotorController::init_motor_pins()
  {
    this->stepper = AccelStepper myStepper(motorInterfaceType, this->pwm_pin, this->direction_pin)
  }

void SentryMotorController::init_motor_settings()
  {
    stepper = this->stepper;
    stepper.setMaxSpeed(this->max_step_speed);
    stepper.setAcceleration(this->acceleration);
  }

void SentryMotorController::spin_cw() 
  {
    stepper = this->stepper;
    stepper.setSpeed(50)
    stepper.runSpeed();
  }

void SentryMotorController::spin_ccw()
  {
    stepper = this->stepper;
    stepper.setSpeed(-50)
    stepper.runSpeed();
  }

void SentryMotorController::stop()
  {
    stepper = this->stepper;
    stepper.stop();
  }