from django.shortcuts import render
import RPi.GPIO as GPIO
import time
channel = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)
# Create your views here.
def jc(request):
	return render(request,'index.html',{})
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
