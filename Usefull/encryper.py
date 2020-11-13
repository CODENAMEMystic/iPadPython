import console, sys
console.clear()

alphabeta = {	'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26, ' ':27, '#':28, '%':29, '^':30, '*':31, '+':32, '=':33,'?':34,'!':35}
#numbOfValues = len(alphabeta)-1



def s2i(input):
	upMessage = input.upper()

	actual = ''
	for y in range(len(upMessage)):
		letter = upMessage[y]
		for value, key in alphabeta.items():
			if letter == value:
				actual += str(key)
	return int(actual)

def p(input):
	print(str(sys.getsizeof(input))+ ' bytes')


into = s2i('Tanner')
key = s2i('9Ahyn#+*^*%!?')

print(into)
print(key)