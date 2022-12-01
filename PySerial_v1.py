import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(port='com3',baudrate=9600,timeout=1)
starttime= time.time()
print("H0")

while True:
	value= ser.readline()
	#value_list=value.split(",")
	#print value_list[1],value_list[2]

	print(value)
	print("H1")
	
	currenttime=int(time.time())
	if (currenttime-starttime)>180:
		starttime=currenttime
	print("H2")
	f=open(str(starttime)+".csv","a")

	line_to_write=str(int(time.time()))+","+str(value)+"\n"
	print("H3")
	
	f.write(line_to_write)
	# f.close()