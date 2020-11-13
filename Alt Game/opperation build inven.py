import time, console

console.clear()


#_________________________________
inventory = {	'wood':20,
							'stick':0,
							'stone':0,
							'wood wall':0
						}
cutWood = 8

#------------------------------------------
def gather():
	action = raw_input('1 - Chop down a tree\n2 - Break off branches\n3 - Gather stone')	
	if action== '1':
		inventory['wood']=inventory['wood']+8
	elif action=='2':
		inventory['stick']=inventory['stick']+4
	elif action=='3':
		inventory['stone']=inventory['stone']+2
#------------------------------------------
def build():
	aBuild= raw_input('1 - Build a wall\n2 - Build a door\n3 - Cut a window\n4 - Build roof')
	if aBuild=='1':
		quantity=raw_input('How many? ')
		if inventory['wood']>=10*quantity:
			print('Not enough wood!')
		else:
			inventory['wood']=inventory['wood']-(10*int(quantity))
			inventory['wood wall']=inventory['wood wall']+int(quantity)
	elif aBuild=='2':
		print('')
	elif aBuild=='3':
		print('')
	elif aBuild=='4':
		print('')
print('Burning Light v2 Opperation\n-------------------\n'+str(inventory)+'\n')
build()
#for key, value in inventory.items():
#	if action==key:
#		print('secondary if complete')
#		inventory[key]=inventory[key]+
			
	
	
print(inventory)
#	if useri == key:
#		group.append(value)
#		print(cGroup)