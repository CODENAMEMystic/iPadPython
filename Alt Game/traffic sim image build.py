from scene import *
import sound
import random
import math
A = Action



class LightNode (SpriteNode):
	def __init__(self, size=(100,100), *args, **kwargs):
		SpriteNode.__init__(self, 'shp:RoundRect' , size=(100,100),*args, **kwargs)
		self.direction='northBound'
		self.color='green'
				
class SelectButton (SpriteNode):
	def __init__(self, size=(100,100), *args, **kwargs):
		SpriteNode.__init__(self, 'shp:RoundRect' , size=(35,35),*args, **kwargs)
		self.id=0
			
	def Activate(self):
		self.ChangeSequence(self.id)
		

class MyScene (Scene):
	def setup(self):
		
		
		
		
		
		
		self.verticleRoad = SpriteNode('VerticleRoad.JPG',parent=self, position=(self.size.w/2, 125))
		self.verticle1Road = SpriteNode('VerticleRoad.JPG',parent=self, position=(self.size.w/2, self.size.h-125))
		
		self.horiRoad = SpriteNode('horizontal.PNG',parent=self, position=(250, self.size.h/2), scale=.5)
		self.horizRoad = SpriteNode('horizontal.PNG',parent=self, position=(self.size.w/2+260, self.size.h/2), scale=.5)
		
		self.intersectionRoad = SpriteNode('intersection.JPG',parent=self, position=(self.size.w/2, self.size.h/2))
		
		
		
		
		
	
		
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		x, y = touch.location
		
		
		
		#if(self.currentSequence<2):
		#	self.currentSequence += 1
		#else:
		#	self.currentSequence = 0
			
	#	self.ChangeSequence(self.currentSequence)
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass
		
		


if __name__ == '__main__':
	run(MyScene(), show_fps=False)