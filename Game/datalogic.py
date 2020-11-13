money = 0
wood = 500
stone = 500
food = 500
mIncrement = 1
wIncrement = 1
sIncrement = 1
fIncrement = 1
#____________________________________________
#SAVE AND LOAD
def load_highscore():
	try:
		with open('.money', 'r') as f:
			global money
			money = int(f.read())
			print(money)
	except:
		money = 0

def save_highscore():
		with open('.money', 'w') as f:
			f.write(str(money))
#__________________________________________________

while True:
	time.sleep(1)
	money = money+mIncrement
	wood = wood+wIncrement
	stone=stone+sIncrement
	food=food+fIncrement
	save_highscore()