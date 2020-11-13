import ui
#from RefineManual import 
test = 'aye'

themeMain = '#666'
themeSecond = '#999'
deck = []



class Card():
	def __init__(self, parent, num, symbol, value):
		self.num = str(num)
		self.symbol = str(symbol)
		self.value = value

		self.x = 430
		self.y = 556
		self.nx = 0
		self.ny = 0
		self.flipped = False
		
		self.base = ui.View(background_color='#FFF')
		self.base.width=100
		self.base.height= self.base.width*1.33
		self.base.border_width=1
		self.base.border_color='black'
		self.base.corner_radius=10
		self.base.x=self.x
		self.base.y=self.y
		
		self.tl = ui.Label()
		self.tl.width=self.base.width/3
		self.tl.height=self.tl.width
		self.tl.x=6
		self.tl.y=6
		self.tl.text=self.num
		self.tl.font=('Futura-Medium',self.base.width/3.75)
		self.tl.alignment=1
		
		self.br = ui.Label()
		self.br.width=self.base.width/3
		self.br.height=self.tl.width
		self.br.x=self.base.width-self.br.width-6
		self.br.y=self.base.height-self.br.height-6
		self.br.text=self.tl.text
		self.br.font=self.tl.font
		self.br.alignment=1
		
		self.m = ui.Label()
		self.m.width=self.base.width/3
		self.m.height=self.tl.width
		self.m.x=self.base.width/2-self.br.width/2
		self.m.y=self.base.height/2-self.br.height/2
		self.m.text=self.symbol
		self.m.font=self.tl.font
		self.m.alignment=1
		
		self.back = ui.View(background_color='#444')
		self.back.width = self.base.width*0.92
		self.back.height = self.base.height*0.92
		self.back.border_width=1
		self.back.border_color='black'
		self.back.corner_radius=10
		self.back.x=6
		self.back.y=6
		
		
		
		self.base.add_subview(self.tl)
		self.base.add_subview(self.br)
		self.base.add_subview(self.m)
		
		
		
		#self.base.add_subview(self.back)
	
		parent.add_subview(self.base)
	
	def moveR(self, x, y):
		self.nx = x
		self.ny = y
	def moveA(self):
		self.base.x = self.nx
		self.base.y = self.ny
	def move(self):
		ui.animate(self.moveA, 1)
		
	def flip(self):
		if self.flipped == False:
			self.flipped = True
			self.base.remove_subview(self.tl)
			self.base.remove_subview(self.br)
			self.base.remove_subview(self.m)
			self.base.add_subview(self.back)
		else:
			self.flipped = False
			self.base.remove_subview(self.back)
			self.base.add_subview(self.br)
			self.base.add_subview(self.m)
			self.base.add_subview(self.tl)
	
		
	def __repr__(self):
		return 'Value: '+self.num+'\nSymbol: '+self.symbol




v = ui.load_view()


deck.append(Card(v, "2", "♠️", 2))

v.present()