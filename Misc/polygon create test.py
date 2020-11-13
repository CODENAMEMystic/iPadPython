from scene import *
import scene, ui, console
console.clear()

scale = 2
class Piece():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

class Polygon(scene.ShapeNode):
	def __init__(self,x,y,z, **kwargs):
		self.x = x
		self.y = y
		self.z = z
		self.w = scale*100
		self.h = scale*50
		path = ui.Path()
		path.line_width = 1
		path.move_to(0, 0)
		path.line_to(scale*50, scale*-25)
		path.line_to(scale*100, scale*0)
		path.line_to(scale*50,scale*25)
		path.close() 
		super().__init__(path, **kwargs)  
		

	
scene
pieces = []
polys = []

#.                  x y z
pieces.append(Piece(0, 0, 0))
#pieces.append(Piece(1, 0, 0))
#pieces.append(Piece(2, 0, 0))
#pieces.append(Piece(3, 0, 0))

def CenterPolys():
	xTot = 0
	yTot = 0
	zTot = 0
	for item in polys:
		if xTot < item.x:
			xTot = item.x+1
		if yTot < item.y:
			yTot = item.y+1
		if zTot < item.z:
			zTot = item.z+1
	print('X Total: '+str(xTot))
	print('Y Total: '+str(yTot))
	return ((xTot+1)*100-(yTot*50)), ((yTot+1)*50)+(xTot*50), zTot

class MyScene(scene.Scene):
	def setup(self):
		self.wAvg = 0.0
		self.hAvg = 0.0
		self.tW = 0.0
		self.tL = 0.0
		self.tH = 0.0
		
		for piece in pieces:
			if piece.z == 0:
				self.wAvg = self.Avg(self.wAvg,piece.x)
				self.hAvg = self.Avg(self.hAvg, piece.y)
				polys.append(Polygon(fill_color='red', stroke_color='green', position=(piece.x*100+100-piece.y*100, piece.x*50+50+piece.y*50), parent=self, x = piece.x, y=piece.y, z=piece.z))
		
			
		#print('heck'+str(self.size.w))
		
		
		
		self.tW,self.tL,self.tH = CenterPolys()
		print(self.tW)
		print(self.tL)
		#print(self.tH)
		
		
		self.cW = (self.size.w/2) 
		self.cH = (self.size.h/2)
		for piece in polys:
			#piece.scale=(1)
			print('thus piece '+str(((self.tW/100))*50))
			piece.position = ( self.cW-((piece.x*100)-(((self.tW/100)-2)*50)), self.cH-((piece.y*100)+ (piece.x*50)- ((self.tL/50)-2)*25))
			#print('Center Width: '+str(self.cW)+' | Piece Pos: '+str(piece.position))
	def Avg(self, average, num):
		average += num
		return average
				

scene.run(MyScene())