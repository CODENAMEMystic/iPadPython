import ui

mainC = '#fff'
headerC = '#e6e6e6'
tableC = '#fbfbfb'


class Order:
	def __init__(self, orderID, orderDate, expense, items):
		self.orderID = orderID
		self.orderDate = orderDate
		self.expenseAmt = expense
		self.returnAmt = 0.0
		self.profit = 0.0
		
		self.items = items
		
		def calculateMoney(self):
			numOfItems = len(self.items)
			self.returnAmt = numOfItems*20
			self.profit = self.returnAmt-self.expenseAmt
		calculateMoney(self)

#Blueberry
blueberryIS = 0; blueberryOrdered = 0
#Citrus
citrusIS = 8; citrusOrdered = 0
#Grape
grapeIS = 0; grapeOrdered = 0
#Mango
mangoIS = 6; mangoOrdered = 0
#Mint
mintIS = 0; mintOrdered = 0
#Pineapple
pineappleIS = 0; pineappleOrdered = 0
#Strawberry
strawberryIS = 0; strawberryOrdered = 0
#Watermelon
watermelonIS = 0; watermelonOrdered = 0

#Devices
eonDeviceChrome = 9
eonDeviceRed = 0
eonDeviceBlue = 0
eonDevicePurple = 0
eonDeviceGold = 0

#Bottles
pineappleBtl = 0
watermelonBtl = 1

#Track Shipments
order1 = Order('9405511298370393268652', '08/20/18', 20, ['citrus','citrus','citrus','citrus'])
order2 = Order('9405511298370393260359', '08/20/18', 20, ['citrus','citrus','citrus','citrus'])
order3 = Order('9405511298370393268997', '08/20/18', 20, ['citrus','citrus','citrus','citrus'])
order4 = Order('9400111298370399173216', '08/14/18', 20, ['citrus','citrus','citrus','citrus'])


notifications = ["8:00a-8:45a - First Hour","8:45a-9:30a - Second Hour", "9:30a-10:15a - Third Hour", "10:15a-11:00a - Fourth Hour"]

def openPage(sender):
	buttonNum = order1.orderID
	if sender.name == 'second':
		buttonNum = order2.orderID
	if sender.name == 'third':
		buttonNum = order3.orderID
	if sender.name == 'fourth':
		buttonNum = order4.orderID
		
		
	print(order1.profit)
	vw.load_url('https://tools.usps.com/go/TrackConfirmAction.action?tLabels='+buttonNum)
	vw.present()

def fillNotifications(v):
	#print(v['scrollview1']["notificationView"]["li1"].text)
	for entry in notifications:
		print(entry)
	a = ui.Label()
	a.text = '1552553'
	
	v['scrollview1']["notificationView"].add_subview(a)
	
		

v = ui.load_view()
fillNotifications(v)
vw = ui.WebView()
vw.load_url('https://tools.usps.com/go/TrackConfirmAction.action?tLabels=9405511298370393268652')
v.background_color = '#3f3f3f'

v.present('fullscreen')