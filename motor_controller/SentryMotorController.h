#ifndef SentryMotorController_h
#define SentryMotorController_h

#include "Arduino.h"
#include "AccelStepper.h"

class SentryMotorController 
  {
    public:
      SentryMotorController(int step_count, int pwm_pin, int direction_pin)
      void spin_cw();
      void spin_ccw();
      void stop();

    private:
      AccelStepper stepper;
      int max_step_speed;
      int acceleration;
      int steps_per_second;
      int pwm_pin;
      int direction_pin;
      void init_motor_pins();
      void init_motor_settings();
  }   

#endif