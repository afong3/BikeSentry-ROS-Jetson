#!/usr/bin/env python
import RPi.GPIO as GPIO

# When this pin is high sentry mode is on
# When pin is low sentry mode is off
# Sentry Mode means motors pan and tilit ssytem is looking for people
# and will file projectiles at peaope when in the stop zone.

ENABLE_PIN = 18 # BCM pin 18, BOARD pin 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENABLE_PIN, GPIO.IN)

def in_sentry_mode():
  return GPIO.input(ENABLE_PIN) == GPIO.HIGH

