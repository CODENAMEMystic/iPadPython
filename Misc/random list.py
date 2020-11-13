import console
console.clear()

a=[1,2]
b=[3,4]
c=[5,6]
d=[7,8]
e=[9,10]
f=[11,12]
g=[13,14]
h=[15,16]
i=[17,18]
j=[19,20]

ab=[a,b]
bb=[c,d]
cb=[e,f]
db=[g,h]
eb=[i,j]

abc=[ab,bb]
bbc=[cb,db]
cbc=[eb]
abcd=[abc,bbc]
bbcd=[cbc]
abcde=[abcd,bbcd]

list = [[[1,2],[3,4]],[[5,6],[7,8]]]

print(abcde)
print('---FIRST---FIRST---FIRST---FIRST---')
for x in abcde:
	print(x)
	print('___SECOND___SECOND___SECOND____SECOND___')
	for y in x:
		print y
		print('===THIRD===THIRD===THIRD===THIRD====')
		for z in y:
			print z
			print('***FOURTH***FOURTH***FOURTH***FOURTH***')
			for a in z:
				print a
				print('+++FIFTH+++FIFTH+++FIFTH+++FIFTH+++')
				for b in a:
					print b
					print('~~~~~~~~~~~~~~~~~~~~')

