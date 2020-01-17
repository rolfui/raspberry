import RPi.GPIO as GPIO
import time

GREEN=23
YELLOW=24
RED=25
BUTTON = 8
GREEN_TIME=15
BUTTON_IDLE_TIME=5

def ledOn(color,duration):
   GPIO.setup(color,GPIO.OUT)
   GPIO.output(color,GPIO.HIGH)
   time.sleep(duration)
   GPIO.output(color,GPIO.LOW)

def btnInit():
   GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   print("btn setup")

def ledInit():
   print("ledInit")
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(GREEN,GPIO.OUT)
   GPIO.setup(YELLOW,GPIO.OUT)
   GPIO.setup(RED,GPIO.OUT)
   GPIO.output(GREEN,GPIO.LOW)
   GPIO.output(YELLOW,GPIO.LOW)
   GPIO.output(RED,GPIO.HIGH)

def greenToRed():
   print("greenToRed")
   GPIO.output(GREEN,GPIO.LOW)
   GPIO.output(YELLOW,GPIO.HIGH)
   time.sleep(3)
   GPIO.output(YELLOW,GPIO.LOW)
   GPIO.output(RED,GPIO.HIGH)

def redToGreen():
   time.sleep(BUTTON_IDLE_TIME)
   GPIO.output(YELLOW,GPIO.HIGH)
   time.sleep(3)
   GPIO.output(RED,GPIO.LOW)
   GPIO.output(YELLOW,GPIO.LOW)
   GPIO.output(GREEN,GPIO.HIGH)


ledInit()
btnInit()
#time.sleep(5)
#greenToRed()
while True:
   btnState = GPIO.input(BUTTON)
   if btnState == False:
      redToGreen()
      time.sleep(GREEN_TIME)
      greenToRed()
   #print(btnState)
   #time.sleep(1)

#time.sleep(10)
#GPIO.output(red,GPIO.LOW)
