#!/usr/bin/python
import RPi.GPIO as GPIO
import time
#GPIO SETUP
channel = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)
x=0
while(x<20):

	if GPIO.input(channel):
		print( " No Water Detected!")
		time.sleep(1)
	else:
		print ("Water Detected!")
		time.sleep(1)
	x=x+1
