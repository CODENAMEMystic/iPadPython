import console, random
console.clear()

numOfPlayers = 4

suit = ['♠️','♥️','♣️','♦️']
rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
deck = []
boardO = []
players = []

valPair = 2
valTwoPair = 3
valStraight = 5
valFlush = 6



sBoard = ''

#p1Hand = []
#p2Hand = []



class Player:
	def __init__(self, num):
		self.playerNum = num
		self.hand = []
		self.handValues = []
		self.endHand = []
		self.sHand = ''
		self.endValue = 0
		
		self.highCard = None
		self.hasPair = False
		self.hasPocketPair = False
		self.pair = []	#if player has pair, specify which card makes a pair
		self.intPair = []
		self.pairValue = 0
		self.hasStraight = False
		self.straight = []	#if player has a straight, specify the straight
		self.hasFlush = False
		self.flush = []	#if player has flush, specify the flush
		
		self.nums = {	'heart':0,
									'club':0,
									'diamond':0,
									'spade':0
								}
		
		self.numOfHearts = 0
		self.numOfDiamonds = 0
		self.numOfClubs = 0
		self.numOfSpades = 0
		
	def finalize(self):
		if self.hasPair:
			print('+ Has a pair')
			#print('Pair: '+str(self.pair))
		if self.hasStraight:
			print('+ Has a straight')
		if self.hasFlush:
			print('+ Has a flush')
		
	def countSuit(self):
		for card in self.hand:
			if card.suit == '♠️':
				self.numOfSpades += 1			
			elif card.suit == '♥️':
				self.numOfHearts += 1
			elif card.suit == '♣️':
				self.numOfClubs += 1
			else:
				self.numOfDiamonds += 1
			self.handValues.append(card.rankValue)
			self.handValues.sort()
			
		self.nums.update(heart=self.numOfHearts, club = self.numOfClubs, diamond=self.numOfDiamonds, spade=self.numOfSpades)
		
		
		

	def __str__(self):
		return('Player '+str(self.playerNum)+'\n'+self.sHand)

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.tSuit = ''
		self.rankValue = None
		
	def Initialize(self):
		#set suit to string
		if self.suit == '♠️':
			self.tSuit = 'spade'
		elif self.suit == '♥️':
			self.tSuit = 'heart'
		elif self.suit == '♣️':
			self.tSuit = 'club'
		else:
			self.tSuit = 'diamond'
	#set rank value
		
		if self.rank == 'J':
			self.rankValue = 11
		elif self.rank == 'Q':
			self.rankValue = 12
		elif self.rank == 'K':
			self.rankValue = 13
		elif self.rank == 'A':
			self.rankValue = 14
		else:
			self.rankValue = int(self.rank)
			
	def __str__(self):
		return(self.rank+self.suit)

class Board:
	def __init__(self):
		self.table = []
		self.sTable = ''
		self.numOfHearts = 0
		self.numOfDiamonds = 0
		self.numOfClubs = 0
		self.numOfSpades = 0
		self.nums = {	'heart':0,
									'club':0,
									'diamond':0,
									'spade':0
								}
		self.highCardAssumption = []
		self.playersWithFlush = []
		self.playersWithStraight = []
		self.playersWithPair = []
		self.pairComparison = [] #Have all players with pair value in here
		
	def convertTableToString(self):
		for card in self.table:
			self.sTable += str(card)+', '
	
	#Count the total of each suit on table
	def countSuit(self):
		for card in self.table:
			if card.suit == '♠️':
				self.numOfSpades += 1			
			elif card.suit == '♥️':
				self.numOfHearts += 1
			elif card.suit == '♣️':
				self.numOfClubs += 1
			else:
				self.numOfDiamonds += 1
		self.nums.update(heart=self.numOfHearts, club = self.numOfClubs, diamond=self.numOfDiamonds, spade=self.numOfSpades)
		
	def __str__(self):
		return(str(self.sTable)+'\nSpades: '+str(self.numOfSpades)+' Hearts: '+str(self.numOfHearts)+' Clubs: '+str(self.numOfClubs)+' Diamonds: '+str(self.numOfDiamonds))

	
board = Board()


#--- DEBUG
def debugPlayerHands():
	for p in players:
		print(p)
		for c in p.hand:
			print(c)

def debugGame():
	print('Board')
	print(sBoard)
	for p in players:
		print(p)
def numOfSuits():
	print(board)

def lineBreak():
	print('---------------------------\n')
	
def debugPlayers():
	for player in players:
		print('Player '+str(player.playerNum))
		print('Value: '+str(player.endValue))
		
#_________




#--- Fill Players
for x in range(numOfPlayers):
	players.append(Player(x))


#--- Standard Deck Setup
#Adds each type of card to deck
for r in rank:
	for s in suit:
		deck.append(Card(s,r))

#Shuffle the deck
random.shuffle(deck)

#Debug - Print deck
#for c in deck: 
#	print(c.rank+c.suit)

#print('OOOOOOOOOOOOOOOO')

#End of Debug

#--- Dispense Player Hands

for x in range(2):
	for p in players:
		deck[0].Initialize()
		p.hand.append(deck[0])
		del deck[0]
#--- Dispence Flop

#Burn first card
del deck[0]
#Place 3 cards
for x in range(3):
	deck[0].Initialize()
	board.table.append(deck[0])
	boardO.append(deck[0])
	del deck[0]

#--- Dispence Last Cards
for x in range(2):
	#burn first card
	del deck[0]
	#place 1 card
	deck[0].Initialize()
	board.table.append(deck[0])
	boardO.append(deck[0])
	del deck[0]

#Player hands and board should be complete now.

#--- Initialize Variables
for c in boardO:
	sBoard += str(c)+', '
for p in players:
	for c in p.hand:
		p.sHand += str(c)+', '

board.countSuit()
board.convertTableToString()
for player in players:
	player.countSuit()

debugGame()
#numOfSuits()
#--- Calculate who won

#is flush available? if not 
availableFlushSuit = None
numOfFlushCards = 0	#var for later comparison

if board.numOfClubs >= 3:
	availableFlushSuit = 'club'
	numOfFlushCards = board.numOfClubs
elif board.numOfHearts >= 3:
	availableFlushSuit = 'heart'
	numOfFlushCards = board.numOfHearts
elif board.numOfSpades >= 3:
	availableFlushSuit = 'spade'
	numOfFlushCards = board.numOfSpades
elif board.numOfDiamonds >= 3:
	availableFlushSuit = 'diamond'
	numOfFlushCards = board.numOfDiamonds

#remove later
'''
lineBreak()
print('Available Flush Suit: '+str(availableFlushSuit))
print('Number of '+str(availableFlushSuit)+': '+str(numOfFlushCards))
lineBreak()
'''
#end

#print('START OF WORK ZONE')
for player in players:
#	lineBreak()
#	print('Player '+str(player.playerNum))
	#print(player.cardValues)
	for c in player.hand:
		player.endHand.append(c.rankValue)
	for c in board.table:
		player.endHand.append(c.rankValue)
#	print('Player hand: '+str(player.hand[0])+', '+str(player.hand[1]))
#	print(sorted(player.endHand))
	
#	lineBreak()
#print('END OF WORK ZONE')




#--- High Card
'''
Find means in which using high card is only calculated either A. if nothing else exists, and B. if there are similar hands between two or more players.
'''
# revise use of sorted(player.handvalues)


	

#--- Pair

for player in players:
	player.endHand.sort()
	
	testCard = player.endHand[0]
	numOfPairs = 0
	for x in range(len(player.endHand)-1):
		if testCard == player.endHand[x+1]:
			numOfPairs += 1
		testCard = player.endHand[x+1]
	
	
	#Check if player has pocket pair
	if player.hand[0].rankValue == player.hand[1].rankValue:
		print('POCKET PAIR')
		player.hasPair = True
		player.pair.append(player.hand[0])
		player.intPair.append(player.hand[0].rankValue)
#		board.playersWithPair.append(player)
		board.pairComparison.append(player.hand[0].rankValue)
		player.hasPocketPair = True
	else:
		#For each card in players hand
		for card in player.hand:
			#For each card on table
			for tCard in board.table:
				#if players card = table card:
				if card.rankValue == tCard.rankValue:
					player.hasPair = True
					player.pair.append(card)
					player.intPair.append(card.rankValue)
					board.pairComparison.append(card.rankValue)
	
	#Add player to the boards 'player with pairs'
	if player.hasPair:
		board.playersWithPair.append(player)
#				print('Player '+str(player.playerNum))
#				print('Card: '+str(card.rankValue)+' + Table: '+str(tCard.rankValue))
#				lineBreak()
#				print(player.pair)
		
	''' #10/28|1:31pm - moving to evaluate players individually to different function
	#Assign value for Num of pairs
	if numOfPairs == 1:
		player.endValue += 2 
	if numOfPairs == 2:
		player.endValue += 3
	if numOfPairs == 3:
		player.endValue += 4
	if numOfPairs == 4:
		player.endValue += 8
	'''
	
		

#--- Straight
#lineBreak()
#print('START OF WORK ZONE')


for player in players:
#	print('player '+str(player.playerNum)) #debug
#	print(set(player.endHand))
	
	
	count = 0
	playerHandSet = set(player.endHand)
	for x in range(len(player.endHand)-1):
		if count != 5:
			if player.endHand[x] == player.endHand[x+1]-1:
				count += 1
			count = 0
	if count == 5:
		player.hasStraight = True
		board.playersWithStraight.append(player)
		#player.endValue += 5 #Moved to reevaluate
		print('PLAYER HAS STRAIGHT')


#print('END OF WORK ZONE')
#lineBreak()
#--- Flush
#if flush is available:
if availableFlushSuit != None:
	#print('+ A flush is available!')
	lineBreak()
	#check if players have matching suit to flush suit
	for player in players:
		if player.nums[availableFlushSuit] != 0:
			if player.nums[availableFlushSuit]+numOfFlushCards >= 5:
				
				player.hasFlush = True
				
				'''
				10/28 - 1:47pm
				try to get all cards that player and table has to make a flush
				
				''
				for card in player.endHand:
					if card.tSuit == availableFlushSuit:
						player.flush.append(card)
				'''
				player.endValue += 6
				print('Player '+str(player.playerNum))
				print('PLAYER CURRENTLY HAS A FLUSH')
				lineBreak()
				#	+	If a player has made it here, they have a FLUSH	+
				# check to see if they have a STRAIGHT FLUSH
				
	if player.hasFlush:
		board.playersWithFlush.append(player)
		
'''
#ABSOLUTE DEBUG ABSOLUTE DEBUG
print('Board Variables')
lineBreak()
print('Players with Pairs')
print(board.playersWithPair)
lineBreak()
print('Players with straight')
print(board.playersWithStraight)
lineBreak()
print('players with flush')
print(board.playersWithFlush)
#END OF ABSOLUTE DEBUG END OF ABSOLUTE
'''

if len(board.playersWithFlush) > 1:
	print('Players with a flush')
	for player in board.playersWithFlush:
		print(player)
elif len(board.playersWithFlush) == 1:
	board.playersWithFlush[0].endValue += valFlush

if len(board.playersWithStraight) > 1:
	print('Players with a straight')
	for player in board.playersWithStraight:
		print(player)
elif len(board.playersWithStraight) == 1:
	board.playersWithStraight[0].endValue += valStraight

lineBreak()
if len(board.playersWithPair) > 1:
	numOfMultiPair = 0
	megaPairs = []
	megaPairValue = []
	for player in board.playersWithPair:
		#if player has more than 1 pair:
		if len(player.pair) > 1:
			#Increase Number Of Players with more than 1 pair
			numOfMultiPair += 1 
			megaPairs.append(player)
			print('MORE THAN ONE PAIR')
			print(player)
			print('Num of players with more than one pair: '+str(numOfMultiPair))
	#If there are no players with more than 1 pair:
	if numOfMultiPair == 0:
		pairValue = []
		print('players with a pair')
		#sort all single pairs all players have from small to large
		board.pairComparison.sort()
		#winning pair = largest pair in list
		winningPair = board.pairComparison[len(board.pairComparison)-1]
		#for player in list of players with a pair:
		for player in board.playersWithPair:
			print(player)
			for card in player.hand:
			#	print('Card: '+str(card.rankValue)+' Winning Value: '+str(winningPair))
				#if card is equal to winning card:
				player.pairValue += card.rankValue
				#if card.rankValue == winningPair:
					#player.endValue += 0.5
					#print('replace me shit')
			pairValue.append(player.pairValue)
		pairValue.sort()
		winningPairMatched = False
		numOfPlayersWithWinningPair = 0
		winningPairPlayers = []
#		print(board.playersWithPair)
		for player in board.playersWithPair:
			player.intPair.sort()
#			print('Testing player '+str(player.playerNum))
#			print('Does player have winning pair?')
#			print('Player.Pair: '+str(player.intPair[len(player.intPair)-1])+' Winning Pair: '+str(winningPair))
#			print(player.intPair[len(player.intPair)-1] == winningPair)
			if player.intPair[len(player.intPair)-1] == winningPair:
				numOfPlayersWithWinningPair += 1
				winningPairPlayers.append(player)
#		print('Winning Pair Players '+str(winningPairPlayers))
		if len(winningPairPlayers) > 1:
			for player in winningPairPlayers:
				if player.pairValue == pairValue[len(pairValue)-1]:
						player.endValue += valPair
		elif len(winningPairPlayers) == 1:
			winningPairPlayers[0].endValue += valPair
						
			#for card in player.hand:
				#if card.rankValue == winningPair:
					#winningPairMatched = True
					#player.endValue += 2
					#if player.pairValue == pairValue[len(pairValue)-1]:
						#player.endValue += 2
				
			
	else:
		winningPairPlayers = []
		winningPair = board.pairComparison[len(board.pairComparison)-1]
		#if there is only one player with three or more of a kind:
		if len(megaPairs) == 1:
			megaPairs[0].endValue += valTwoPair
		#if there is more than one player with three or more of a kind:
		if len(megaPairs) > 1:
			print('more than one player with three or more of a kind')
			#add combination of card pair values
			for player in megaPairs:
				for card in player.hand:
					player.pairValue += card.rankValue
				print('Player '+str(player.playerNum)+' Pair Value: '+str(player.pairValue))
				megaPairValue.append(player.pairValue)
				megaPairValue.sort()
				megaPairWinningValue = megaPairValue[len(megaPairValue)-1]
			for player in megaPairs:
				if player.pairValue == megaPairWinningValue:
					player.endValue += valTwoPair
					
		for player in board.playersWithPair:
			player.intPair.sort()
#			print('Testing player '+str(player.playerNum))
#			print('Does player have winning pair?')
#			print('Player.Pair: '+str(player.intPair[len(player.intPair)-1])+' Winning Pair: '+str(winningPair))
#			print(player.intPair[len(player.intPair)-1] == winningPair)
			if player.intPair[len(player.intPair)-1] == winningPair:
				winningPairPlayers.append(player)
				
#		print('Winning Pair Players '+str(winningPairPlayers))
		if len(winningPairPlayers) > 1:
			for player in winningPairPlayers:
				if player.pairValue == pairValue[len(pairValue)-1]:
						player.endValue += valPair
		elif len(winningPairPlayers) == 1:
			winningPairPlayers[0].endValue += valPair
				
			
		
		
elif len(board.playersWithPair) == 1:
	#print('one pair')
	print(board.playersWithPair[0])
	board.playersWithPair[0].endValue += valPair

if len(board.playersWithFlush) > 1:
	print('fuck me with this shit')
elif len(board.playersWithFlush) == 1:
	board.playersWithFlush[0].endValue += valFlush


for player in players:
	if player.endValue == 0:
		sorted(player.handValues)
		player.endValue = player.handValues[1]/10
		
lineBreak()
print('DEBUG: Players End Value')
for player in players:
	print('Player '+str(player.playerNum))
	print(player.endValue)
	

lineBreak()
testVal = players[0].endValue
winner = players[0]
for player in players:
	if player.endValue > testVal:
		winner = player
print('Winner is Player '+str(winner.playerNum))







	


'''
i have pairs working to an extent gowever i come accross the problem of when a hand say with a pair of twos and an Ace is compares to a pair of threes and a king, it supposes that vecause ace is high card that it won out of the pair
'''

'''
10/28 - 2:34pm
last i have edited was pair evaluation, so far it works in regards to figuring out whether a player card matches to the board and can diferentiate between three of a kind and what not however, pairs in player hands do not register.
'''