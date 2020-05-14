import RPi.GPIO as GPIO
import time


RED=25  #GPIO-number

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,GPIO.LOW)

GPIO.output(RED,GPIO.HIGH)
time.sleep(2)
GPIO.output(RED,GPIO.LOW)
