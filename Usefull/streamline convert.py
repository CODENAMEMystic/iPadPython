import console
console.clear()

tempK = '0A 0A 0A'

#Inputed message: ABCD
input = 1020304050
#Test: Can input be divisible by: 2,3,4,5?



#def input):
maxCount = 0
x = 2
maxInt = 1
while x <= 5:
	tempCount = 0
	tinput = input
	if tinput % x == 0:
		while tinput % x == 0:
			#print tinput
			#print 'number: '+str(x)
			tinput = tinput / x
			tempCount += 1
		if tempCount > maxCount:
			maxCount = tempCount
			maxInt = x
	x += 1
print maxInt
print maxCount

if maxInt != 1:
	while input % maxInt == 0:
		input = input / maxInt
		#LOG how many times
print input


new = {}
x = 0
while input != 0:
	value = input % 100
	input = input / 100
	new[x] = value
	x += 1	

	








#print newNumber


newNumber = {}
x = 0
max = len(newNumber)
b2 = True
while b2 == True:
	number = 1
	if number == 1:
		b2 = False
		#print 'Complete: '+str(number)
		

#print len(newNumber)