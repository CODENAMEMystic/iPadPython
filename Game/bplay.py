import ui
import console
import time
money=5
wood=6
stone=7
food=8
Money = 'Money: ' + str(money)
Wood = 'Wood: ' +str(wood)
Stone = 'Stone: ' +str(stone)
Food = 'Food: ' +str(stone)
 
Miner=1
Lumberjack=1
StoneMasonary=1
Farmer=4

MinerPurchase=10
MinerRefund=round(MinerPurchase/1.5)

LumberjackPurchase=10
LumberjackRefund= round(LumberjackPurchase/1.5)

StoneMasonaryPurchase=10
StoneMasonaryRefund=round(StoneMasonaryPurchase/1.5)

FarmerPurchase=10
FarmerRefund=round(FarmerPurchase/1.5)


raidText = 'User has raided the '
loadText = 'Loading Saved Data'


#______________________________________________________________________


#______________________________________________________________________

#ACTION DEFINITIONS
def location_start():
	location = console.alert('Location','Select your starting location','Plains','Mountains', 'Other','true')
	if location == 1:
		storyText.text='Plains'
	if location == 2:
		storyText.text='Mountains'
	if location == 3:
		storyText.text='Other'
def army_tapped(sender):
	print('')
def work_tapped(sender):
	work_prompt.present('sheet')
def raid_tapped(sender):
	sRaid = console.alert('Raid','Select who to raid', 'Argentis Archers', 'Barbaric Barbarians', 'Wizardly Wizards')
	if sRaid == 1:
		storyText.text=raidText + str('Argentis Archers')
	if sRaid == 2:
		storyText.text=raidText +str('Barbaric Barbarians')
	else:
		storyText.text=raidText +str('Wizardly Wizards')
def info_tapped(sender):
	storyText.text='Info'
	
def buy_Miner(sender):
	global money
	global Miner
	global MinerPurchase
	global mIncrement
	if money >= MinerPurchase:
		money = money-MinerPurchase
		Miner = Miner+1
		mIncrement = round(mIncrement*2)
		RVMoney.text = Money
		MinerPurchase = round(MinerPurchase*1.5)
		buyMiner.title= 'Buy: ' +str(MinerPurchase)
		MinerLabel.text = 'Miner: ' +str(Miner)
		
	else:
		print('ERROR: Not enough money')
	
#____________________________________________________________________
	
																												#UI DEFINITIONS
#Storyboard
storyText = ui.Label(background_color= 'grey')
storyText.alignment= 1
storyText.text='Story Text'
storyText.width=800
storyText.height=250
#MoneyText
moneyText = ui.Label(background_color='lightgray')
moneyText.alignment= 0
moneyText.text=Money
moneyText.width=100
moneyText.height=30
moneyText.x=25
moneyText.y=10
#Wood Text
woodText = ui.Label(background_color='lightgray')
woodText.alignment= 0
woodText.text=loadText
woodText.width=100
woodText.height=30
woodText.x=284
woodText.y=10
#Stone Text
stoneText = ui.Label(background_color='lightgray')
stoneText.alignment= 0
stoneText.text=loadText
stoneText.width=100
stoneText.height=30
stoneText.x=540
stoneText.y=10
#Food Text
foodText = ui.Label(background_color='lightgray')
foodText.alignment= 0
foodText.text=loadText
foodText.width=100
foodText.height=30
foodText.x=796
foodText.y=10
#Army Button
army = ui.Button(title='Army',background_color= 'gray')
army.action = army_tapped
army.x=25
army.y=75
army.width=200
army.height=50
#Work
work = ui.Button(title='Work', background_color= 'gray')
work.action = work_tapped
work.x=284
work.y=75
work.width=200
work.height=50
#Info
info = ui.Button(title='Info', background_color= 'gray')
info.action = info_tapped
info.x=540
info.y=75
info.width=200
info.height=50
#Raid
raid = ui.Button(title='Raid', background_color= 'gray')
raid.action = raid_tapped
raid.x=796
raid.y=75
raid.width=200
raid.height=50
																											#UI DEFINITIONS - SHAPES
#Shelf Layers
shelf = ui.View(background_color='lightgray')
shelf.width=1024
shelf.height=150
shelf.y=550
#Top Shelf
topShelf = ui.View(background_color='gray')
topShelf.width=1024
topShelf.height=50

																													#WORK PROMPT UI
work_prompt = ui.View(background_color='lightgray')
work_prompt.width=512
work_prompt.height=600

upgradeList = ui.View(background_color='gray')
upgradeList.width=500
upgradeList.height= 580
upgradeList.x=6
upgradeList.y=10
ULW = 200 #Upgrade Label Width
ULH = 50  #Upgrade Label Height
UBW = 125 #Upgrade Button Height

#-------------MINER VIEW--------#

ResourceView = ui.View(background_color='lightgreen')
ResourceView.width=480
ResourceView.height=ULH+10
ResourceView.x=10
ResourceView.y=10

RVMoney = ui.Label(background_color='lightgray')
RVMoney.alignment=1
RVMoney.text=Money
RVMoney.width=ResourceView.width/2 - 7.5
RVMoney.height=ULH
RVMoney.x=5
RVMoney.y=5

RVFood = ui.Label(background_color='lightgray')
RVFood.alignment=1
RVFood.text=Food
RVFood.width=RVMoney.width
RVFood.height=RVMoney.height
RVFood.x=RVMoney.x+RVMoney.width+5
RVFood.y=RVMoney.y



MinerView = ui.View(background_color='lightgreen')
MinerView.width=480
MinerView.height=ULH+10
MinerView.x=ResourceView.x
MinerView.y=ResourceView.y+ULH+20

MinerLabel = ui.Label(background_color='lightgray')
MinerLabel.alignment=1
MinerLabel.text="Miner: " +str(Miner)
MinerLabel.width=ULW
MinerLabel.height=ULH
MinerLabel.x=5
MinerLabel.y=5

buyMiner = ui.Button(title='Buy: '+str(MinerPurchase), background_color='lightgray')
buyMiner.action = buy_Miner
buyMiner.width=UBW
buyMiner.height=ULH
buyMiner.x= MinerLabel.x +ULW+10
buyMiner.y= MinerLabel.y

sellMiner =ui.Button(title='Sell: '+str(MinerRefund), background_color='lightgray')
sellMiner.width=buyMiner.width
sellMiner.height=buyMiner.height
sellMiner.x= buyMiner.x+buyMiner.width+5
sellMiner.y= buyMiner.y

LumberjackView = ui.View(background_color='lightgreen')
LumberjackView.width=480
LumberjackView.height=ULH+10
LumberjackView.x= MinerView.x
LumberjackView.y= MinerView.y+ULH+20

LumberjackLabel = ui.Label(background_color='lightgray')
LumberjackLabel.alignment=1
LumberjackLabel.text='Lumberjack: ' +str(Lumberjack)
LumberjackLabel.width=ULW
LumberjackLabel.height=ULH
LumberjackLabel.x= 5
LumberjackLabel.y= 5

buyLumberjack = ui.Button(title='Buy: '+str(LumberjackPurchase), background_color='lightgray')
buyLumberjack.width=UBW
buyLumberjack.height=ULH
buyLumberjack.x= LumberjackLabel.x +ULW +10
buyLumberjack.y= LumberjackLabel.x

sellLumberjack=ui.Button(title='Sell: '+str(LumberjackRefund), background_color='lightgray')
sellLumberjack.width=buyLumberjack.width
sellLumberjack.height=buyLumberjack.height
sellLumberjack.x=buyLumberjack.x+buyLumberjack.width+5
sellLumberjack.y=buyLumberjack.y

StoneMasonaryView = ui.View(background_color='lightgreen')
StoneMasonaryView.width=480
StoneMasonaryView.height=ULH+10
StoneMasonaryView.x= LumberjackView.x
StoneMasonaryView.y= LumberjackView.y+ULH+20

StoneMasonaryLabel = ui.Label(background_color='lightgray')
StoneMasonaryLabel.alignment=1
StoneMasonaryLabel.text='Stone Masonary: ' +str(StoneMasonary)
StoneMasonaryLabel.width=ULW
StoneMasonaryLabel.height=ULH
StoneMasonaryLabel.x=5
StoneMasonaryLabel.y=5

buyStoneMasonary = ui.Button(title='Buy: '+str(StoneMasonaryPurchase),background_color='lightgray')
buyStoneMasonary.width= UBW
buyStoneMasonary.height= ULH
buyStoneMasonary.x = StoneMasonaryLabel.x +ULW+10
buyStoneMasonary.y = StoneMasonaryLabel.y

sellStoneMasonary = ui.Button(title='Sell: '+str(StoneMasonaryRefund), background_color='lightgray')
sellStoneMasonary.width=buyStoneMasonary.width
sellStoneMasonary.height=buyStoneMasonary.height
sellStoneMasonary.x=buyStoneMasonary.x+buyStoneMasonary.width+5
sellStoneMasonary.y=buyStoneMasonary.y



FarmerView = ui.View(background_color='lightgreen')
FarmerView.width=480
FarmerView.height=ULH+10
FarmerView.x=StoneMasonaryView.x
FarmerView.y=StoneMasonaryView.y+ULH+20

FarmerLabel = ui.Label(background_color='lightgray')
FarmerLabel.alignment=1
FarmerLabel.text='Farmer: ' + str(Farmer)
FarmerLabel.width=ULW
FarmerLabel.height=ULH
FarmerLabel.x=5
FarmerLabel.y=5

buyFarmer=ui.Button(title='Buy: '+str(FarmerPurchase), background_color='lightgray')
buyFarmer.width=UBW
buyFarmer.height=ULH
buyFarmer.x=FarmerLabel.x+ULW+10
buyFarmer.y= FarmerLabel.y

sellFarmer=ui.Button(title='Sell: '+str(FarmerRefund), background_color='lightgray')
sellFarmer.width=buyFarmer.width
sellFarmer.height=buyFarmer.height
sellFarmer.x=buyFarmer.x+buyFarmer.width+5
sellFarmer.y=buyFarmer.y

#INITIALIZE UI
vp = ui.View(background_color='white')
storyText.center = (vp.width * 5, vp.height * 1)
#--------Structure-----------#

#--Main View Includes-----#
vp.add_subview(shelf)
		#-----Shelf----#
shelf.add_subview(topShelf)
				#---Top Shelf---#
topShelf.add_subview(moneyText)
						#--Money Text---#
topShelf.add_subview(woodText)
						#---Wood Text---#
topShelf.add_subview(stoneText)
						#--Stone Text---#
topShelf.add_subview(foodText)
						#---Food Text---#
shelf.add_subview(army)
				#--Army Button--#
shelf.add_subview(work)
				#--Work Button--#

						#--Work Prompt--#
work_prompt.add_subview(upgradeList)
						#--Upgrade List--#
upgradeList.add_subview(ResourceView)
ResourceView.add_subview(RVMoney)
ResourceView.add_subview(RVFood)
upgradeList.add_subview(MinerView)
						#-----Miner View-----#
MinerView.add_subview(MinerLabel)
						#-----Miner Label----#
MinerView.add_subview(buyMiner)
MinerView.add_subview(sellMiner)
upgradeList.add_subview(LumberjackView)
LumberjackView.add_subview(LumberjackLabel)
LumberjackView.add_subview(buyLumberjack)
LumberjackView.add_subview(sellLumberjack)

upgradeList.add_subview(StoneMasonaryView)
StoneMasonaryView.add_subview(StoneMasonaryLabel)
StoneMasonaryView.add_subview(buyStoneMasonary)
StoneMasonaryView.add_subview(sellStoneMasonary)

upgradeList.add_subview(FarmerView)
FarmerView.add_subview(FarmerLabel)
FarmerView.add_subview(buyFarmer)
FarmerView.add_subview(sellFarmer)
				#----Farmer View-----#



vp.add_subview(storyText)



shelf.add_subview(raid)
shelf.add_subview(info)




#load_highscore()
vp.present()



