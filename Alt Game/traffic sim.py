import console, time, random
console.clear()

carPerMinute = 1
flow = 2

#A simple intersection, no roads just entry


#The light sequence
class Intersection():
	def __init__(self):
		self.sequence = 0
		self.southR = 0
		self.northR = 0
		self.westR = 0
		self.eastR = 0
		self.waited = 0
		
	
	def switchSequence(self):
		self.waited = 0
		if self.sequence >= 2:
			self.sequence = 0
		else:
			self.sequence += 1
	
	
		
	def doStuff(self, tick):
		carPerMinute = random.randint(0,2)
		
		if self.waited >= 6:
			a.switchSequence()
		if(self.sequence == 0):
			self.southR += getCars()
			self.northR += getCars()
			self.westR += getCars()
			self.eastR += getCars()
			if tick % 6 == 0:
				self.sequence += 1
			
		if(self.sequence == 1):
			if self.southR != 0:
				self.southR -= flow
				if self.southR < 0:
					self.southR = 0
			
			else:
				self.waited += 1
			if self.northR != 0:
				self.northR -= flow
				if self.northR < 0:
					self.northR = 0
			else:
				self.waited += 1
			self.westR += getCars()
			self.eastR += getCars()
			
			
		if self.sequence == 2:
			if self.westR != 0:
				self.westR -= flow
				if self.westR < 0:
					self.westR = 0
			else:
				self.waited += 1
			if self.eastR != 0:
				self.eastR -= flow
				if self.eastR < 0:
					self.eastR = 0
			else:
				self.waited += 1
			self.northR += getCars()
			self.southR += getCars()
			
def getCars():
		return random.randint(0,3)
		
a = Intersection()



waited = 0

tick = 1
while tick < 100:
	time.sleep(1)
	console.clear()
	
	a.doStuff(tick)
	if tick % 10 == 0:
		a.switchSequence()
	
	tick += 1
	print('North: ' + str(a.northR))
	print('South: ' + str(a.southR))
	print('West: '+str(a.westR))
	print('East: '+str(a.eastR))
	print('Sequence: ' +str(a.sequence))
	print('Waited: '+str(a.waited))