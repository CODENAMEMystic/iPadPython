import console, math
console.clear()

#---NOTES
#Encryptor can potentially be created one of many ways.
	#Example one - encryptor converts letter to number defined in alphabeta
	#Example two - encryptor converts letter into other letter based on new assignment of value in alphabeta
#Potential rules:
	#take note of position in message to determine rule to execute
	

alphabeta = {	'A':10,'B':20,'C':30,'D':40,'E':50,'F':60,'G':70,'H':80,'I':90,'J':11,'K':12,'L':13,'M':14,'N':15,'O':16,'P':17,'Q':18,'R':19,'S':21,'T':22,'U':23,'V':24,'W':25,'X':26,'Y':27,'Z':28, ' ':29}

alphaRomaeta = {	'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':21,'X':23,'Y':24,'Z':25} 

message = 'ABCD'
Key = '1A'


#______________________________________
def Encrypt(message):
	
	messageLength = len(message)
	encryptedM = ''
	finalMessage = ''
	for pos in range(messageLength):
		letter = message[pos]
		for value, key in alphabeta.items():
			if value == letter:
				encryptedM += str(key)
				
	#Run following after complete
	
	encryptInteger = int(encryptedM)	
	count = 1
	while encryptInteger % 2 == 0:	
		#print 'Debug: ' + str(encryptInteger)
		encryptInteger = encryptInteger/2
		count += 1
		
	
	
	
#--- Create key for decrypting
	temp = count % 10
	count = count / 10
	for inc, value in alphaRomaeta.items():
		if count == value:
			alphaExponent = inc			
	#example key: 0A1B2C
	Key = (str(temp) + alphaExponent)
#_______________________________________________
	#print encryptInteger
	d1 = encryptInteger
	print d1
	
	print 'Key: '+ Key

	return str(encryptInteger)
	
	
	
	

	
def Decrypt(message):
	global key
	
	intMessage = int(message)
	decryptedM = ''
	d1 = Key[0:2]
	count = d1[0]
	alphaExponent = d1[1]
	for key, value in alphaRomaeta.items():
		if alphaExponent == key:
			alphaExponent = (value*10)
	multiplier = (int(count)+alphaExponent)
	
	
	while multiplier != 1:
		intMessage = intMessage * 2
		multiplier -= 1
		print intMessage
		#create while loop to have exponent maths done. 
	
	
	#newMessage = str(message)	
	numberLength = len(str(intMessage))/2
	
	
	for number in range(numberLength):	
		time = 0
		time += 2
		
		numberZ = str(intMessage)[number*time:number*time+2]
		
		for key, value in alphabeta.items():
			if value == int(numberZ):
				decryptedM += key
	return decryptedM
#_________________________________________________
	
	
	
	
 
#print 'Message: ' + message
run1 = Encrypt(message)

print 'Encrypt: ' + run1


#enMessage = Encrypt(message)
#print 'Decrypt: ' + Decrypt(enMessage)