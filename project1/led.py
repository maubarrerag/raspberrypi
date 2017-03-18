#!/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)

def Blink(speed):
	while(True):
		GPIO.output(7, True)
		time.sleep(speed)
		GPIO.output(7, False)
		time.sleep(speed)

Blink(5)
