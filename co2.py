import time
import serial
import RPi.GPIO as GPIO

GREEN=23
YELLOW=24
RED=25

CO2HIGH=1500
CO2OK=800

ser = serial.Serial(
   port="/dev/ttyS0",
   baudrate = 9600,
   parity = serial.PARITY_NONE,
   stopbits = serial.STOPBITS_ONE,
   bytesize = serial.EIGHTBITS,
   timeout = 1
)

def ledInit():
   print("ledInit")
   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)
   GPIO.setup(GREEN,GPIO.OUT)
   GPIO.setup(YELLOW,GPIO.OUT)
   GPIO.setup(RED,GPIO.OUT)
   GPIO.output(GREEN,GPIO.LOW)
   GPIO.output(YELLOW,GPIO.LOW)
   GPIO.output(RED,GPIO.LOW)

def co2Init():
   #ser.write("A 32\r\n")
   #ser.write("M 310\r\n")
   #ser.write("M 2\r\n")
   #ser.write(".\r\n")
   #ser.write("a\r\n")
   ser.write("K 2\r\n")
   #ser.write("G\r\n")
   #ser.write("u 0\r\n")
   time.sleep(2)
   ser.readline()

def co2Read():
   ser.write("Z\r\n")
   time.sleep(1)
   str=ser.readline().split()
   co2=10*int(str[1])
   return co2

def setLED(color):
   GPIO.output(GREEN,GPIO.LOW)
   GPIO.output(YELLOW,GPIO.LOW)
   GPIO.output(RED,GPIO.LOW)
   GPIO.output(color,GPIO.HIGH)

ledInit()
co2Init()


while True:
   co2Level=co2Read()
   if co2Level < CO2OK:
      setLED(GREEN)
   elif co2Level > CO2HIGH:
      setLED(RED)
   else:
      setLED(YELLOW)
   print(co2Level)
