class PCM:
	def __init__(self):
		self.createRIFFChunk()
		self.createFMTChunk()
		self.createDATAChunk()
		
		self.setRIFFChunk()
		self.setFMTChunk()
		self.setDATAChunk()
		self.finalBytes = bytearray()      #when all byte arrays concatenated together
		self.fieldList = [self.chunkID, self.chunkSize, self.format,              \
						  self.subChunkID1, self.subChunk1Size, self.audioFormat, \
						  self.numberChannels, self.sampleRate, self.byteRate,    \
						  self.blockAlign, self.bitsPerSample, self.subChunkID2,  \
						  self.subChunk2Size, self.data]
		
	def createRIFFChunk(self):
		self.chunkID   = bytearray()
		self.chunkSize = bytearray()
		self.format    = bytearray()
	
	def createFMTChunk(self):
		self.subChunkID1     = bytearray()
		self.subChunk1Size   = bytearray()
		self.audioFormat     = bytearray()
		self.numberChannels  = bytearray()
		self.sampleRate      = bytearray()
		self.byteRate        = bytearray()
		self.blockAlign      = bytearray()
		self.bitsPerSample   = bytearray()
	
	def createDATAChunk(self):
		self.subChunkID2   = bytearray()
		self.subChunk2Size = bytearray()
		self.data = bytearray()
		
	def setRIFFChunk(self):
		self.setByteArray(self.chunkID, "RIFF") #little endian is RIFF
		self.setByteArray(self.format, "WAVE")
	
	def setFMTChunk(self):
		self.setByteArray(self.subChunkID1, "fmt ")
		self.setByteArray(self.subChunk1Size, [16,0,0,0])
		self.setByteArray(self.audioFormat, [1,0])
		self.setByteArray(self.numberChannels, [1,0])
		self.setByteArray(self.sampleRate, [68,172,0,0]) #68 is 0x44 and 172 is 0xAC
		self.setByteArray(self.byteRate, [68,172,0,0]) # samplerate * numberchannels * (size of sample/8)
		self.setByteArray(self.blockAlign, [1,0])
		self.setByteArray(self.bitsPerSample, [8,0])
	
	def setDATAChunk(self):
		self.setByteArray(self.subChunkID2, "data")
	
	def setByteArray(self, field, data):
		for i in data:
			if str(type(i)) == "<class 'str'>":
				field.append(ord(i))
			else:
				field.append(i)
		
	
	def byteWrite(self, byte):
		self.data.append(byte)
	
	def setSize(self):
		size = hex(4 + 8 + 16 + 8 + len(self.data))
		if len(size) > 6:
			firstByte = size[2:3]
			secondByte = size[3:5]
			thirdByte = size[5:]
			fourthByte = '0'
			
		elif len(size) > 4:
			firstByte = size[2:4]
			secondByte = size[4:]
			thirdByte = '0'
			fourthByte = '0'
		else:
			firstByte = size[2:4]
			secondByte = '0'
			thirdByte =  '0'
			fourthByte = '0'
		print(size)
			
		self.setByteArray(self.chunkSize, [int(thirdByte,16), int(secondByte,16), \
										   int(firstByte, 16), int(fourthByte, 16)])
		
		print(self.chunkSize)
		
		size = hex(len(self.data))
		if len(size) > 6:
			firstByte = size[2:3]
			secondByte = size[3:5]
			thirdByte = size[5:]
			fourthByte = '0'
			
		elif len(size) > 4:
			firstByte = size[2:4]
			secondByte = size[4:]
			thirdByte = '0'
			fourthByte = '0'
		else:
			firstByte = size[2:4]
			secondByte = '0'
			thirdByte =  '0'
			fourthByte = '0'
		print(size)
			
		self.setByteArray(self.subChunk2Size, [int(thirdByte,16), int(secondByte,16), \
										       int(firstByte, 16), int(fourthByte, 16)])
	
	def setFinalByteState(self):
		for i in self.fieldList:
			self.finalBytes += i 
		
		
	def fileWrite(self, filename):
		self.setSize()
		self.setFinalByteState()
		file = open(filename + '.wav', 'wb')
		file.write(self.finalBytes)
		file.close()
	
	
		
		
		
		
		
		
		
		
		
		