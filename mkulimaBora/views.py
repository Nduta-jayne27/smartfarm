from django.shortcuts import render
from .models import farmdata
import RPi.GPIO as GPIO
import time
channel = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)

import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
pin=4


# Create your views here.
def jc(request):
	return render(request,'index.html',{})
def kc(request):

	message=""
	hum=""
	temp=""
	if request.method == 'GET':
		humidity,temparature=Adafruit_DHT.read(sensor,pin)
		if humidity is not None and temparature is not None:
                	hum= '{0:0.1f}%'.format(humidity)
                	temp= '{0:0.1f}*'.format(temparature)
                	main=farmdata(humidity=hum,temparature=temp)
                	main.save()
                	print( hum + temp)
		else:
                	print('Failed to get reading. Try again!')
		if GPIO.input(channel):
			message="Water The Farm"
			print( " No Water Detected!")
		else:
			message="Water Level is Okay"
			print( "Water Detected!")
	return render(request,'irrigation.html',{'msg':message,'hum':hum,'temp':temp})
