import RPi.GPIO as GPIO
import time

GREEN=23
YELLOW=24
RED=25
BUTTON = 8

def btnInit():
   print("btn setup ...")
   GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def ledInit():
   print("ledInit ...")
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(GREEN,GPIO.OUT)
   GPIO.output(GREEN,GPIO.LOW)

def ledOn(LED):
   GPIO.output(LED,GPIO.HIGH)

ledInit()
btnInit()

while True:
   btnState = GPIO.input(BUTTON)
   if btnState == False:
      ledOn(GREEN)
      time.sleep(2)
