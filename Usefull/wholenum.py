import console
console.clear()

num = 10
factor = 3

out = []

nums = []

class Num():
	def __init__(self, n):
		self.n = n
		self.o = []
		self.ou = []
		
		def doStuff(self):
			#a = self.n
			
			factor = 1
			x = 0
			while x < 9:
				a = self.n
				out = []
				factor += 1
				while a/factor % 1 == 0:
					a /= factor
					out.append(int(a))
				self.o.append(out)
				x +=1
		doStuff(self)
		
	def __str__(self):
		return(	'2: '+str(self.o[0])+'\n'
						'3: '+str(self.o[1])+'\n'
						'4: '+str(self.o[2])+'\n'
						'5: '+str(self.o[3])+'\n'
						'6: '+str(self.o[4])+'\n'
						'7: '+str(self.o[5])+'\n'
						'8: '+str(self.o[6])+'\n'
						'9: '+str(self.o[7])+'\n'
						'10: '+str(self.o[8])
						)

def fillClass():
	for x in range(26):
		y = (x+1)*10
		a = Num(y)
		nums.append(a)
	


fillClass()
ab = len(nums)

while ab > 0:
	print('-------------'+str(nums[ab-1].n)+'-------------')
	print(str(nums[ab-1]))
	print()
	ab = ab - 1
	