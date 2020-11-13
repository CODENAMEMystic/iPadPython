import ui, console
console.clear()
a = ui.Button
e = "Empty"

#BOARD = {	"A1":"wRook1",		"A2":"wPawn1", "A3":e, "A4":e, "A5":e, "A6":e, "A7":"bPawn1", "A8":"bRook1",
#					"B1":"wKnight1",	"B2":"wPawn2", "B3":e, "B4":e, "B5":e, "B6":e, "B7":"bPawn2", "B8":"bKnight1",
#					"C1":"wBishop1",	"C2":"wPawn3", "C3":e, "C4":e, "C5":e, "C6":e, "C7":"bPawn3",	"C8":"bBishop1",
#					"D1":"wKing",			"D2":"wPawn4", "D3":e, "D4":e, "D5":e, "D6":e, "D7":"bPawn4",	"D8":"bKing",
#					"E1":"wQueen",		"E2":"wPawn5", "E3":e, "E4":e, "E5":e, "E6":e, "E7":"bPawn5",	"E8":"bQueen",
#					"F1":"wBishop2",	"F2":"wPawn6", "F3":e, "F4":e, "F5":e, "F6":e, "F7":"bPawn6",	"F8":"bBishop2",
#					"G1":"wKnight2",	"G2":"wPawn7", "G3":e, "G4":e, "G5":e, "G6":e, "F7":"bPawn7",	"G8":"bKnight2",
#					"H1":"wRook2",		"H2":"wPawn8", "H3":e, "H4":e, "H5":e, "H6":e, "H7":"bPawn8",	"H8":"bRook2"
#				}
gameboard = {}






def button(sender):
	#print(sender.superview[sender.name].name) #Debug good to note for future
	
	if sender.selected == False: #If button was selected
		sender.selected = True
		sender.border_width = 5
		sender.border_color = 'blue'
		for x in sender.superview.subviews: #unselect all other buttons
			if x.name != sender.name:
				x.selected=False
				x.border_color='ffffff'
				
	else:	#otherwise deselect
		sender.selected = False
		sender.border_width = 0
		sender.border_color = 'ffffff'
		
	#print('Selected? '+ str(sender.selected)) #Debug





v = ui.load_view()
v.present('full')