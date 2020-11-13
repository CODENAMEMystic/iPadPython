from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):
		#print(self.size.h)
		s = SpriteNode('images/stonePath.JPG', position=(100, 200), scale=(.1))
		g = SpriteNode('images/grass.PNG', position=(300, 200), scale=(.1))
		

		
		
#--- Create Ground
		ground = Node(parent=self)
		tio = ['images/grass.PNG', 'images/stonePath.JPG']
		#grass
		for y in range(13):
			for x in range(17):
				a = random.randint(0,1)
				tile = SpriteNode(tio[a], position=(x*60, y*60), scale=(.24), anchor_point = (0, 0))
				tile.gridPos = (x,y)
				
				ground.add_child(tile)
		
		
		self.tick = 0
	def removes(self):
		self.ground.pop
	def did_change_size(self):
		pass
	
	def update(self):
		if self.tick % 20 == 0:
			
			self.setup()
		self.tick+=1
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass
		
		
	
	

		

if __name__ == '__main__':
	run(MyScene(), show_fps=True)