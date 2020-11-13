import ui, console
console.clear()

headerFontColor = '#4378e0'
balance = 0
age = 0
jobsText = 'Infant'
profession = 'Infant'
storyText = ''


def ageBtn_pressed(sender):
	global age, storyText
	scrollView = sender.superview['scrollView']
	
	newLbl = ui.Label()
	newLbl.width = scrollView.width - 24
	newLbl.height = 100
	newLbl.x = 12
	newLbl.y = scrollView.lines * 100+6
	newLbl.number_of_lines = 0
	newLbl.text = 'Age: '+str(age)+'\n'
	newLbl.text += 'the most of the words that could possibly be said in ones scroll view and what is this i have just recieved an email that i i will now go and read as soon as i am done looking or rather typing what ever i am typign right now and jesus christ why is it that i only use my left hand much more than my right hand right now like holy hell look at this typing speed'
	
	scrollView.text = storyText
	scrollView.content_size = (scrollView.width, (scrollView.lines+1) * 100 +6)
	scrollView.add_subview(newLbl)
	
	scrollView.lines += 1
	age += 1
	print(scrollView.lines * 50+6)
	
v = ui.load_view()
v.present()
