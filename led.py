import RPi.GPIO as GPIO
import time

red = 24
yellow = 18
green = 25
btn = 23


def ledOn(color,duration):
   GPIO.setup(color,GPIO.OUT)
   GPIO.output(color,GPIO.HIGH)
   time.sleep(duration)
   GPIO.output(color,GPIO.LOW)

def btnInit():
   GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   print("btn setup")

def ledInit():
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(red,GPIO.OUT)
   GPIO.setup(yellow,GPIO.OUT)
   GPIO.setup(green,GPIO.OUT)
   GPIO.output(red,GPIO.LOW)
   GPIO.output(yellow,GPIO.LOW)
   GPIO.output(green,GPIO.HIGH)

def greenToRed():
   GPIO.output(green,GPIO.HIGH)
   time.sleep(2)
   GPIO.output(green,GPIO.LOW)
   GPIO.output(yellow,GPIO.HIGH)
   time.sleep(3)
   GPIO.output(yellow,GPIO.LOW)
   GPIO.output(red,GPIO.HIGH)

def redToGreen():
   GPIO.output(red,GPIO.HIGH)
   time.sleep(2)
   GPIO.output(yellow,GPIO.HIGH)
   time.sleep(3)
   GPIO.output(red,GPIO.LOW)
   GPIO.output(yellow,GPIO.LOW)
   GPIO.output(green,GPIO.HIGH)


ledInit()
btnInit()
#time.sleep(5)
greenToRed()
while True:
   btnState = GPIO.input(btn)
   if btnState == False:
      redToGreen()
      time.sleep(10)
      greenToRed()
   #print(btnState)
   #time.sleep(1)

#time.sleep(10)
#GPIO.output(red,GPIO.LOW)
