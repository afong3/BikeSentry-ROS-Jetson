#ifndef WheelMotorController_h
#define WheelMotorController_h

#include "Arduino.h"

class WheelMotorController 
  {
    public:
      WheelMotorController(int speed, int enable_a_pin, int in_1_pin, int in_2_pin);
      void start_spin();
      void stop_spin();

    private:
      int speed;
      int enable_a_pin;
      int in_1_pin;
      int in_2_pin;
      void init_motor_pins();
  };   

#endif
