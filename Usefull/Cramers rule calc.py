import console
console.clear()
print("Cramers Rule Calculator\n")


a1=1
b1=-1
c1=-4
a2=-4
b2=4
c2=4
#X=((c1*b2)-(b1*c2))/((a1*b2)-(b1*a2))
#Y=((a1*c2)-(c1*a2))/((a1*b2)-(b1*a2))

#-----------------
print('Equation:')
if(b1>=0):
	print(str(a1)+' + '+str(b1)+' = '+str(c1))
else:
	print(str(a1)+'  '+str(b1)+' = '+str(c1))
if(b2>=0):
	print(str(a2)+' + '+str(b2)+' = '+str(c2)+'\n')
else:
	print(str(a2)+' '+str(b2)+'='+str(c2)+'\n')
#-----------------
	
print('		|	'	+	str(c1)	+	'	 '	+	str(b1)	+	'	|							|		'	+	str(a1)	+	'		'	+	str(c1)	+	'	|\n'
			'		|	'	+	str(c2)	+	'	 '	+	str(b2)	+	'	|							|		'	+	str(a2)	+	'		'	+	str(c2)	+	'	|\n'
			'X =		--------------				Y =		--------------	\n'
			'		|	'	+	str(a1)	+	'	 '	+	str(b1)	+	'	|							|		'	+	str(a1)	+	'		'	+	str(b1)	+	'	|\n'
			'		|	'	+	str(a2)	+	'	 '	+	str(b2)	+	'	|							|		'	+	str(a2)	+	'		'	+	str(b2)	+	'	|\n'
			)
print('Step 1:	('+str(c1)+' * '+str(b2)+') = '+str(c1*b2))
print('Step 2:	('+str(c2)+' * '+str(b1)+') = '+str(c2*b1)+'\n-------')
print('Step 3:	('+str(c1*b2)+' - '+str(c2*b1)+') = '+str(c1*b2-c2*b1))

print('\nStep 4:	('+str(a1)+' * '+str(b2)+') = '+str(a1*b2))
print('Step 5:	('+str(a2)+' * '+str(b1)+') = '+str(a2*b1)+'\n-------')
print('Step 6:	('+str(a1*b2)+' - '+str(a2*b1)+') = '+str(a1*b2-a2*b1))

print(str((c1*b2-c2*b1)/(a1)))
print('X = '+ str(X))
print('Y = '+ str(Y))