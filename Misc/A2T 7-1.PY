import console, math
console.clear()

def ex():
	print 'Bobby bought a car for $50,000. How much would his car be worth in 5 years if the value depreciates 5% each year'
	
	q = 50000
	w = 0.05
	e = 2
	print 'a = $50,000 | car value'
	print 'b = 0.05 | growth/decay percent'
	print 'x = 5 | time increment'
	r = q*w
	while e != 0:
		t = r * e
		e -= 1
	print q - t
	




ex()

print('y = a + b^x\n')

a = input('Enter a ')
b = input('Enter b ')
x = input('Enter x ')

y = a + math.pow(1+b, x)
print y