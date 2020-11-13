import ui




selectedT = 0
def convert(inport):
	if(inport == 'A.M.'):
		return 0
	elif(inport == 'P.M.'):
		return 1
	
def update(view):
	ap1 = convert(view.superview['sapLbl'].text)
	ap2 = convert(view.superview['eapLbl'].text)
	
	
	hour1 = int(view.superview['shourLbl'].text)
	hour2 = int(view.superview['ehourLbl'].text)
	
	minute1 = int(view.superview['sminuteLbl'].text)
	minute2 = int(view.superview['eminuteLbl'].text)
	
	if(ap1 == 1):
		hour1 += 12
	elif(ap2 == 1):
		hour2 += 12
		
	view.superview['thourLbl'].text=str(hour1)
	view.superview['tminuteLbl'].text=str(hour2)
		

def button_pressed(sender):
	if sender.superview.superview['seg'].selected_index == 0:
		sender.superview.superview['shourLbl'].text = sender.title
	else:
		sender.superview.superview['ehourLbl'].text = sender.title
	update(sender.superview)

def mButton_pressed(sender):
	if sender.superview.superview['seg'].selected_index == 0:
		sender.superview.superview['sminuteLbl'].text = sender.title
	else:
		sender.superview.superview['eminuteLbl'].text = sender.title
	update(sender.superview)

def apButton_pressed(sender):
	if sender.superview['seg'].selected_index == 0:
		sender.superview['sapLbl'].text = sender.title
		if(sender.superview['sapLbl'].text == 'P.M.'):
			sender.superview['eapLbl'].text='P.M.'
			
		
	else:
		sender.superview['eapLbl'].text = sender.title
	update(sender)
	
def seg_sel(sender):
	selectedT= sender.selected_index
	
	if(sender.superview['sapLbl'].text=='P.M.'):
		
		if(sender.selected_index == 1):
			sender.superview['amBtn'].enabled = False
			
		else:
			sender.superview['amBtn'].enabled = True
	update(sender)


	
v = ui.load_view()
v.present('full') 
