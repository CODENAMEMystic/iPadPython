import console, time
	
class Dot():
	def __init__(self, pos):
		self.pos = pos
		self.forward = -10
		self.backward = 0
		self.space = ' '
		self.output = '•'
	def u(self):
		if self.forward-self.pos < 118:
			self.output = self.space*(self.forward-self.pos)
			self.forward += 1
		elif self.forward-self.pos == 118:
			self.backward = self.forward
			self.forward +=1
		elif self.backward-self.pos > 0:
			self.output = self.space*(self.backward-self.pos)
			self.backward -= 1
		elif self.backward-self.pos == 0:
			self.forward = self.backward
		self.output += '•'
		print(self.output)
	
dots = []
var = 20
unt = 0
for x in range(25):
	if unt < var:
		dots.append(Dot(unt))
		unt+=1
	else:
		while unt > 0:
			unt -=1
			dots.append(Dot(unt))
	
for x in range(600):
	for dot in dots:
		dot.u()
	time.sleep(.01)
	console.clear()