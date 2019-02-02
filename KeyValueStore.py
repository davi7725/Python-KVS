import os

class KVS:
	filepath = ""
	hashmap = {}
	def __init__(self, path):
		self.filepath = path
		self.hashMap = {}
		if(os.path.isfile(self.filepath)):
			self.PopulateHashMap()
		else:
			f = open(self.filepath, "a+")
			f.close()
			
	def PopulateHashMap(self):
		index = ""
		pos = 0
		c = ""
		flag = True
		
		f = open(self.filepath, "r")
		
		while(f.tell() != os.path.getsize(self.filepath)):
			c = f.read(1)
			if(c == "," and flag == True):
				flag = False
				self.hashMap[index] = pos
				index = ""
			
			if(flag):
				index += c
			
			if(c == "\n" and flag == False):
				pos = f.tell()
				flag = True
				
		f.close()
		
		
	def SetData(self, index, value):
		lastOffset = os.path.getsize(self.filepath)
		self.hashMap[index] = lastOffset
		f = open(self.filepath, "a+")
		f.write(index + "," + value + "\n")
		f.close()
		
	def GetData(self, index):
		offset = self.hashMap[index]
		value = ""
		
		f = open(self.filepath, "r")
		
		f.seek(offset + len(index) + 1,0)
		c = f.read(1)
		
		while(c != "\n" and f.tell() != os.path.getsize(self.filepath)):
			value += c
			c = f.read(1)
		f.close()
		
		return (index, value)
		
	def GetAll(self):
		tuppleArray = []
		for key in self.hashMap:
			tuppleArray.append(self.GetData(key))
		return tuppleArray