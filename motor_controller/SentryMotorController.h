#ifndef SentryMotorController_h
#define SentryMotorController_h

#include "Arduino.h"
#include "AccelStepper.h"

class SentryMotorController 
  {
    public:
      SentryMotorController(int step_count, int pwm_pin, int direction_pin, int enable_pin);
      void set_max_speed(int val);
      void set_acceleration(int val);
      void spin_cw();
      void spin_ccw();
      void disable_motor();
      void enable_motor();

    private:
      AccelStepper stepper;
      int max_step_speed;
      int acceleration;
      int steps_per_second;
      int pwm_pin;
      int direction_pin;
      int enable_pin;
      void init_motor_pins();
      void init_motor_settings();
  };   

#endif
