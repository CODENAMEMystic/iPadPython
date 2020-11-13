from scene import *
import sound, console
import random
import math
A = Action
console.clear()


class MyScene (Scene):
	def setup(self):
		self.background_color = '#00b'
		self.gridPoints = []
		self.xPoints = 5
		self.yPoints = 5
		
		self.makeGrid()
	
	def makeGrid(self):
		widthInt = self.size.width / self.xPoints
		heightInt = self.size.height / self.yPoints
		
		x = 0
		y = 0
		
		while x < self.xPoints:
			
			while y < self.yPoints:
				point = ( math.ceil(x*widthInt), math.ceil(y*heightInt))
				self.gridPoints.append(point)
				y += 1
			x+=1
			y = 0
		print(self.gridPoints)
		
			
	def did_change_size(self):
		pass
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)