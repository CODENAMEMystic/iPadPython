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

class Location (SpriteNode):
	def __init__(self, size=(100,100), *args, **kwargs):
		SpriteNode.__init__(self, 'shp:RoundRect' , size=(35,35),*args, **kwargs)
		self.name = str()
		


class Vehicle (SpriteNode):
	def __init__(self, size=(100,100), *args, **kwargs):
		SpriteNode.__init__(self, 'spc:CockpitGreen2' , size=(35,35),*args, **kwargs)
		
		self.potentialDestinations = ['northBound','eastBound', 'southBound', 'westBound']
		self.origin
		self.destination = ''
		
		
def createMap(self):
		map = []
		map.append(SpriteNode('VerticleRoad.JPG',parent=self, position=(self.size.w/2, 125)))
		map.append(SpriteNode('VerticleRoad.JPG',parent=self, position=(self.size.w/2, self.size.h-125)))
		
		map.append(SpriteNode('horizontal.PNG',parent=self, position=(250, self.size.h/2), scale=.5))
		map.append(SpriteNode('horizontal.PNG',parent=self, position=(self.size.w/2+260, self.size.h/2), scale=.5))
		
		map.append(SpriteNode('intersection.JPG',parent=self, position=(self.size.w/2, self.size.h/2)))
		
		return map
		
class MyScene (Scene):
	def setup(self):
		createMap(self)
		
		self.cars = []
		
		
		self.destinations =[]
		
		
		self.currentSequence = 0
		
		self.seq0 = SelectButton(parent=self,position=(50,self.size.height-50))
		self.seq1 = SelectButton(parent=self,position=(100,self.size.height-50))
		self.seq1.id=1
		self.seq2 = SelectButton(parent=self,position=(150,self.size.height-50))
		self.seq2.id=2
		
		self.startB = SelectButton(parent=self,position=(200,self.size.height-50))
		
		
			
	
		
		
		
		self.northbound = LightNode(parent=self, anchor_point=(0,0.5),position=(self.size.w/2+25 ,self.size.h/2+120), scale=0.25)
		
		self.southbound = LightNode(parent=self, anchor_point=(0,0.5),position=(self.size.w/2-45 ,self.size.h/2-120),scale=0.25)
		self.southbound.direction='southBound'
		
		self.westbound = LightNode(parent=self, anchor_point=(0,0.5),position=(self.size.w/2-120 ,self.size.h/2+25),scale=.25)
		self.westbound.direction='westBound'
		
		self.eastbound = LightNode(parent=self, anchor_point=(0,0.5),position=(self.size.w/2+100 ,self.size.h/2-25),scale=0.25)
		self.eastbound.direction='eastBound'
		
		self.southSpawn = (self.size.w/2+30, 200)
		
		
		
		
		self.group=[]
		self.group.append(self.northbound)
		self.group.append(self.eastbound)
		self.group.append(self.southbound)
		self.group.append(self.westbound)
	
	
	def createVehicle(self, cars):
		cars.append(Vehicle(parent=self, position=(self.southSpawn)))
		
	def ChangeSequence(self, sequence):
		for light in self.group:
			if(light.direction=='northBound' or light.direction=='southBound'):
				if(sequence==0):
					light.color='red'
				if(sequence==1):
					light.color='green'
				if(sequence==2):
					light.color='red'
					
			if(light.direction=='eastBound' or light.direction=='westBound'):
				if(sequence==0):
					light.color = 'red'
				if(sequence==1):
					light.color = 'red'
				if(sequence==2):
					light.color='green'
					
		
		 
	
	def update(self):
		pass
			
	
	def touch_began(self, touch):
		x, y = touch.location
		
		if(x > 20 and x < 75 and y > self.size.h - 70 ):
			self.ChangeSequence(0)
		if(x > 80 and x < 125 and y > self.size.h - 70 ):
			self.ChangeSequence(1)
		if(x > 140 and x < 175 and y > self.size.h - 70 ):
			self.ChangeSequence(2)
		
		if(x > 200 and x < 225 and y > self.size.h - 70 ):
			self.createVehicle(self.cars)
		
		
		#if(self.currentSequence<2):
		#	self.currentSequence += 1
		#else:
		#	self.currentSequence = 0
			
	#	self.ChangeSequence(self.currentSequence)
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass
		
		
	def tile_for_touch(self, touch):
		touch_pos = self.point_from_scene(touch.location)
		for t in self.group:
			if t.frame.contains_point(touch_pos):
				return t
			else:
				print('fuck')


if __name__ == '__main__':
	run(MyScene(), show_fps=False)