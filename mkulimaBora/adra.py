import Adafruit_DHT
import time
sensor=Adafruit_DHT.DHT11
pin=4
while True:
	humidity,temparature=Adafruit_DHT.read(sensor,pin)
	if humidity is not None and temparature is not None:
		print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temparature, humidity))
	else:
		print('Failed to get reading. Try again!')
	time.sleep(3)
