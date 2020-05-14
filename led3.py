import RPi.GPIO as GPIO
import time


RED=25  #GPIO-number
BUTTON = 8

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,GPIO.LOW)

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.1)
    btnState = GPIO.input(BUTTON)
    #print(btnState)
    if btnState == False:
        GPIO.output(RED,GPIO.HIGH)
    else:
        GPIO.output(RED,GPIO.HIGH)
