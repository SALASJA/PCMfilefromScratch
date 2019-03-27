from PCM import PCM
from math import *
def main():
	wave = PCM()
	frequency = round(44100/261.6)
	halfwave = 44100 / 440 /2/2/2 #this is 333
	time = 44100 * 5
	count = 0
	state = True
	while(count < time):
		secondByte = round(110 * sin(count/halfwave) + 127.5)     #writing the byte file in little endian
		count = count + 1
		#wave.byteWrite(round(110 * sin(count/ halfwave) + 110))
		firstByte = round(110 * sin(count/halfwave) + 127.5)
		count = count + 1
		if count < time:
			wave.byteWrite(secondByte)
			wave.byteWrite(firstByte)
		
	wave.fileWrite("filename")
		

main()
