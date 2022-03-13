#include "SentryMotorController.h"

#define motorInterfaceType 1

SentryMotorController::SentryMotorController(int steps_per_second, int pwm_pin, int direction_pin, int enable_pin) 
  {
    this->max_step_speed = 1000;
    this->acceleration = 50;
    this->steps_per_second = steps_per_second; 
    this->pwm_pin = pwm_pin;
    this->direction_pin = direction_pin;
    this->enable_pin = enable_pin;
    this->init_motor_pins();
    this->init_motor_settings();
  } 

void SentryMotorController::set_max_speed(int val)
  {
    this->max_step_speed = val;
  }

void SentryMotorController::set_acceleration(int val)
  {
    this->acceleration = val;
  }

void SentryMotorController::init_motor_pins()
  {
    AccelStepper stepper(motorInterfaceType, this->pwm_pin, this->direction_pin);
    this->stepper = stepper;
  }

void SentryMotorController::init_motor_settings()
  {
    AccelStepper stepper = this->stepper;
    stepper.setMaxSpeed(this->max_step_speed);
    stepper.setAcceleration(this->acceleration);
  }

void SentryMotorController::spin_cw() 
  {
    AccelStepper stepper = this->stepper;
    this->enable_motor();
    stepper.setSpeed(50);
    stepper.runSpeed();
  }

void SentryMotorController::spin_ccw()
  {
    AccelStepper stepper = this->stepper;
    this->enable_motor();
    stepper.setSpeed(-50);
    stepper.runSpeed();
  }

void SentryMotorController::disable_motor()
  {
    int enable_pin = this->enable_pin;
    digitalWrite(enable_pin, HIGH);
  }

void SentryMotorController::enable_motor() 
  {
    int enable_pin = this->enable_pin;
    digitalWrite(enable_pin, LOW);
  }
