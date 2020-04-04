import os
import time
import serial

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

ser = serial.Serial(
   port="/dev/ttyS0",
   baudrate = 9600,
   parity = serial.PARITY_NONE,
   stopbits = serial.STOPBITS_ONE,
   bytesize = serial.EIGHTBITS,
   timeout = 1
)

base_dir = '/sys/bus/w1/devices/'

device_file = [base_dir + '28-00000930655c' + '/w1_slave']
device_file.append(base_dir + '28-00000930882a' + '/w1_slave')

def read_temp_raw(dev):
    f = open(device_file[dev], 'r')
    lines = f.readlines()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = r.readlines()
    f.close()
    return lines

def extract_temp(lines):
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp = float(temp_string) / 1000.0
        return temp

def read_temp():
    lines = [read_temp_raw(0),read_temp_raw(1)]
    temp = [extract_temp(lines[0]),extract_temp(lines[1])]
    return temp

def read_co2():
    try:
        ser.write(str.encode('Z\r\n'))
        line = ser.readline().decode('utf-8')
        co2 =  int(line[3:8]) * 10  # factor of 10 needed to convert to ppm
        return co2
    except:
        return "eeeee"

file_name = 'log-' + time.strftime('%H%M%S', time.localtime()) + '.txt'
print('Filename:' , file_name)
print('Format: HHMMSS, CO2 in ppm, Temperaturer i Celsius:')
while True:
    temp = read_temp();
    tid = time.strftime('%H%M%S', time.localtime())
    co2 = read_co2()
    outString = tid + ',' + f'{co2}'.zfill(5) + ',' + f'{temp[0]:.3f}'.zfill(7) + ','  + f'{temp[1]:.3f}'.zfill(7)
    print(outString)
    f = open(file_name,"a")
    f.write(outString + '\r\n')
    f.close()
    #time.sleep(60)
