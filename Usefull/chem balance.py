import console
MolarMass = {'H':1.01,
						'He':4.00,
						'Li':6.94,
						'Be':9.01,
						'B':10.81,
						'C':12.01,
						'N':14.00,
						'O':16.00,
						'F':19.00,
						'Ne':20.18,
						'Na':22.99,
						'Al':26.98,
						'Si':28.09,
						'P':30.97,
						'S':32.07,
						'Cl':35.45,
						'Ar':39.95,
						'K':30.10,
						'Ca':40.08,
						'Sc':44.96,
						'Ti':47.87,
						'V':50.94,
						'Cr':52.00,
						'Mn':54.94,
						'Fe':55.85,
						'Co':58.93,
						'Ni':58.69,
						'Cu':63.55,
						'Zn':65.41,
						'Ga':69.72,
						'Ge':72.64,
						'As':74.92,
						'Se':78.96,
						'Br':79.90,
						'Kr':83.80,
						'Rb':85.47,
						'Sr':87.62,
						'Y':88.91,
						'Zr':91.23,
						'Cs':132.91,
						'Fr':223,
						}
						
						

def intro():
	console.clear()
	choose = input('Choose which program\n 1 - Sum Molar Mass ')
	if choose == '1':
		enter()
#___________________________ADD_MOLAR_MASS______________
group = []						
def enter():
	useri = input('Enter Chemical Letter...')
	for key, value in MolarMass.items():
		if useri == key:
			group.append(value)
			enter()
			cGroup = sum(group)
			for var in group:
				print(str(var)+' + ')
			print('-----------')
			print(cGroup)
			eSMM = input('Exit? (y/n)')
			if eSMM == 'n':
				enter()
			else:
				print('Thank You')
				intro()

#_______________________________________________________
group1 = ['C','C','B']
group2 = ['C','B','Li']
groupa = set(group1)
groupb = set(group2)
#def balance():
	#useri = raw_input('Enter Chemical Letter...')
	#groupb.append(useri)
	#balance()
	
		



#_______________________________________________________
intro() #Very start *DO NOT DELETE*
#balance()
#_______________________________________________________