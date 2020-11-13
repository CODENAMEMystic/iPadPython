import string
string = string.ascii_letters

password=['zaboiii']
testNumber = 0
found = 0
passGen = []
#
numbers = [1,2,3,4,5,6,7,8,9,0]
letters = {
					0:'a',
					1:'b',
					2:'c',
					3:'d',
					4:'e',
					5:'f',
					6:'g',
					7:'h',
					8:'i',
					9:'j',
					10:'k',
					11:'l',
					12:'m',
					13:'n',
					14:'o',
					15:'p',
					16:'q',
					17:'r',
					18:'s',
					19:'t',
					20:'u',
					21:'v',
					22:'w',
					23:'x',
					24:'y',
					25:'z',
					}
def main():					
	global testNumber, found #Call for global variables
	for key, value in letters.items(): #For key provided, find value in letters items
		if key == testNumber: #if key = test number
			passGen.append(value) #add value to passGen list
			if passGen != password: #if passGen is not equal to password
				passGen.remove(value) #remove passGen's values
				testNumber=testNumber+1 #add 1 to test number
			elif testNumber > 25:
				testNumber= 0
				second()
		#repeat until found
def second():
	global testNumber
	for key, value in letters.items():
		if key == testnumber:
			
		
		
		

			
main()
print('Password: '+ str(passGen) +'Test Number' + str(testNumber))