#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
def cleario():
   
    s=[5, 6, 13, 19, 12]
    for port in s:

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, True)
        time.sleep(0.5)
	
        GPIO.output(port, False)

    GPIO.cleanup()



