from django.shortcuts import render
import RPi.GPIO as GPIO
import time
channel = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)

import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
pin=4

while True:
	humidity,temparature=Adafruit_DHT.read(sensor,pin)
	if humidity is not None and temparature is not None:
		hum= '{0:0.1f}%'.format(humidity)
		temp= '{0:0.1f}*'.format(temparature)
		print( hum + temp)
	else:
		print('Failed to get reading. Try again!')
	time.sleep(3)
# Create your views here.
def jc(request):
	return render(request,'index.html',{'hum':hum,'temp':temp})
def kc(request):

	message=""
	if GPIO.input(channel):
		message="Water The Farm"
		print( " No Water Detected!")
		time.sleep(1)
	else:
		message="Water Level is Okay"
		print( "Water Detected!")
		time.sleep(1)
	return render(request,'irrigation.html',{'msg':message})
