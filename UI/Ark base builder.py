import ui, console
console.clear()
def pressed(sender):
	if sender.hit == False:
		sender.background_color = ('#222')
		sender.hit = True
	else:
		sender.background_color = ('#fff')
		sender.hit = False



def sub(sender):
	output=''
	v = sender.superview
	for view in v.subviews:
		if view.hit == True:
			output+=view.pos+', '
			print('pieces.append(Piece('+view.title+', 0))')
	#print(output)
					

WIDTH = 10
HEIGHT = 10

v = ui.load_view()
for view in v.subviews:
	for x in range(WIDTH):
		for y in range(HEIGHT):
			if view.title == str(y)+str(x):
				#print(view.name)
				pass

for xi in range(WIDTH):
	for yi in range(HEIGHT):
		a = ui.Button(background_color='#fff')
		a.x=xi*50+50
		a.y=yi*50+50
		a.width=40
		a.height=40
		a.border_width=1
		a.name=(str(xi)+str(yi))
		a.title= str(xi)+', '+str(yi)
		a.pos = '('+str(a.x)+', '+str(a.y)+')'
		a.hit=False
		a.action=pressed
		
		v.add_subview(a)

b = ui.Button(background_color='#f5f')
b.x=50
b.y=600
b.width=400
b.height=40
b.border_width=1
b.title='B'
b.hit=False
b.pos=''
b.action=sub
		
v.add_subview(b)
v.present()