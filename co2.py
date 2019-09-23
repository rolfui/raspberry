import time
import serial

ser = serial.Serial(
   port="/dev/ttyS0",
   baudrate = 9600,
   parity = serial.PARITY_NONE,
   stopbits = serial.STOPBITS_ONE,
   bytesize = serial.EIGHTBITS,
#   timeout = 1
)

#ser.write("a\r\n")
#ser.write("K 1\r\n")
while True:
   print(ser.readline())
   time.sleep(1)
