import ui, console, time 

console.clear()

# ---VARIABLES
deck = []



# ---CLASSES
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

def place():
	c = 0
	for card in deck:
		amt = 5 #what does this do?
		print(c)
		if c < 2:
			x = card.base.superview['p1'].x+6 + ((card.base.width/2)*(c))
			y = card.base.superview['p1'].y+6
		elif c < 4:
			x = card.base.superview['p2'].x+6 + ((card.base.width/2)*(c-5))
			y = card.base.superview['p2'].y+6
		elif c < 8:
			for z in range(amt):
				x = card.base.superview['p3'].x+6 + ((card.base.width/2)*(c-10))
				y = card.base.superview['p3'].y+6
		else:
			break
			x = card.base.x
			y = card.base.y
		
		c += 1
		card.moveR(x,y)
		card.move()

	


# ---VIEWS/MISC	
v = ui.load_view()



deck.append(Card(v, "2", "♠️", 2))
deck.append(Card(v, "2", "♣️", 2))
deck.append(Card(v, "2", "♥️", 2))
deck.append(Card(v, "2", "♦️", 2))
deck.append(Card(v, "3", "♠️", 3))
deck.append(Card(v, "3", "♣️", 3))
deck.append(Card(v, "3", "♥️", 3))
deck.append(Card(v, "3", "♦️", 3))
deck.append(Card(v, "4", "♠️", 4))
deck.append(Card(v, "4", "♣️", 4))
deck.append(Card(v, "4", "♥️", 4))
deck.append(Card(v, "4", "♦️", 4))
deck.append(Card(v, "5", "♠️", 5))
deck.append(Card(v, "5", "♣️", 5))
deck.append(Card(v, "5", "♥️", 5))
deck.append(Card(v, "5", "♦️", 5))
deck.append(Card(v, "6", "♠️", 6))
deck.append(Card(v, "6", "♣️", 6))
deck.append(Card(v, "6", "♥️", 6))
deck.append(Card(v, "6", "♦️", 6))
deck.append(Card(v, "7", "♠️", 7))
deck.append(Card(v, "7", "♣️", 7))
deck.append(Card(v, "7", "♥️", 7))
deck.append(Card(v, "7", "♦️", 7))
deck.append(Card(v, "8", "♠️", 8))
deck.append(Card(v, "8", "♣️", 8))
deck.append(Card(v, "8", "♥️", 8))
deck.append(Card(v, "8", "♦️", 8))
deck.append(Card(v, "9", "♠️", 9))
deck.append(Card(v, "9", "♣️", 9))
deck.append(Card(v, "9", "♥️", 9))
deck.append(Card(v, "9", "♦️", 9))
deck.append(Card(v, "10", "♠️", 10))
deck.append(Card(v, "10", "♣️", 10))
deck.append(Card(v, "10", "♥️", 10))
deck.append(Card(v, "10", "♦️", 10))
deck.append(Card(v, "A", "♠️", 10))
deck.append(Card(v, "A", "♣️", 10))
deck.append(Card(v, "A", "♥️", 10))
deck.append(Card(v, "A", "♦️", 10))
deck.append(Card(v, "J", "♠️", 10))
deck.append(Card(v, "J", "♣️", 10))
deck.append(Card(v, "J", "♥️", 10))
deck.append(Card(v, "J", "♦️", 10))
deck.append(Card(v, "Q", "♠️", 10))
deck.append(Card(v, "Q", "♣️", 10))
deck.append(Card(v, "Q", "♥️", 10))
deck.append(Card(v, "Q", "♦️", 10))
deck.append(Card(v, "K", "♠️", 10))
deck.append(Card(v, "K", "♣️", 10))
deck.append(Card(v, "K", "♥️", 10))
deck.append(Card(v, "K", "♦️", 10))

		

v.present()

num = 0
c = 0
for card in deck:
#while num < len(deck):
	if c < 2:
		x = card.base.superview['p1'].x+6 + ((card.base.width+6)*(c))
		y = card.base.superview['p1'].y+6
	elif c < 4:
		x = card.base.superview['p2'].x+6 + ((card.base.width+6)*(c-2))
		y = card.base.superview['p2'].y+6
	elif c < 6:
		#for z in range(amt):
		x = card.base.superview['p3'].x+6 + ((card.base.width+6)*(c-4))
		y = card.base.superview['p3'].y+6
	else:
		break
		x = card.base.x
		y = card.base.y
	
	num +=1
	c += 1
	card.moveR(x,y)
	card.move()
	time.sleep(0.15)