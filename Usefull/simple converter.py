from __future__ import absolute_import
from __future__ import print_function
import console
from six.moves import range
console.clear()

alphabeta = {	'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26, ' ':27, '#':28}
numbOfValues = len(alphabeta)-1


initialMessage = 'you are a turtle for east every nothing'
upMessage = initialMessage.upper()
	
length = list(range(len(upMessage)))
letter = upMessage[0]

variable = 1
increment = numbOfValues - numbOfValues 

encryptString = ''

	
for y in length:
	letter = upMessage[y]
	for value, key in alphabeta.items():
		if letter == value:
			actual = key + variable
			for seckey, secvalue in alphabeta.items():
				if actual == secvalue:
					encryptString += seckey
					
					
print(initialMessage)
print(encryptString)
print()
print('Decrypt: ')

decryptString = ''
for x in length:
	letter = encryptString[x]
	for value, key in alphabeta.items():
		if letter == value:
			actual = key - variable
			if actual > numbOfValues:
				actual = actual - numbOfValues
			while actual > numbOfValues:
				if actual % 2 == 0:
					actual = actual / 2
				else:
					actual = (actual/month) + day
			for seckey, secvalue in alphabeta.items():
				if actual == secvalue:
					decryptString += seckey
					
print(decryptString)
