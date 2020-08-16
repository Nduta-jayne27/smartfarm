import RPi.GPIO as gp
import time
pin =8
gp.setmode(gp.BOARD)
gp.setup(pin,gp.OUT)
for i in range(0,5):
	gp.output(pin,gp.HIGH)
	time.sleep(1)
	gp.output(pin,gp.LOW)
	time.sleep(1)
gp.cleanup()
