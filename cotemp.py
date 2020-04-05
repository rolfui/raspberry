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

dirs = os.listdir(base_dir)
#dirs.remove('w1_bus_master1')
dirs.sort()
dirs.pop()

device_files = []
for dir in dirs:
    device_files.append(base_dir + dir + '/w1_slave')

def read_temp():
    temp = []
    for device_file in device_files:
        f = open(device_file, 'r')
        lines = f.readlines()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = r.readlines()
        f.close()
        equals_pos = lines[1].find('t=')
        temp_string = lines[1][equals_pos+2:]
        temp.append(float(temp_string)/1000.0)
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
while True:
    temp = read_temp();
    tid = time.strftime('%Y%m%d%H%M%S', time.localtime())
    #tid = int(time.time())
    #print(tid)
    co2 = read_co2()
    #outString = str(tid) + ',' + f'{co2}'.zfill(5) + ',' + f'{temp[0]:.3f}'.zfill(7) + ','  + f'{temp[1]:.3f}'.zfill(7)
    #outString = str(tid) + ',' + str(co2) + ',' + str(temp[0]) + ','  + str(temp[1])
    outString = tid + ',' + str(co2)
    for tmp in temp:
        outString +=  ',' + str(tmp)
    print(outString)
    f = open(file_name,"a")
    f.write(outString + '\r\n')
    f.close()
    time.sleep(60)
