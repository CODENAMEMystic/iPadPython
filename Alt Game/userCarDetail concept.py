import console
console.clear()


class Cars():
	def __init__(self):
		self.cars = []
		
	def addCar(self, car):
		self.cars.append(car)
					
	def __str__(self):
		list = ''
		for car in self.cars:
			list += ' '+str(car )
		return 'Vehicles:\n'+self.list

class Vehicle():
	def __init__(self, year, make, model, trim):
		self.year = year
		self.make = make
		self.model = model
		self.trim = trim
		self.color = str()
		
		self.transmission = str()
		self.drivetrain = str()
		
		self.tags = []
		
		
	def addTag(self, tags):
		for tag in tags:
			self.tags.append(tag)
					
	def __str__(self):
		return 'Vehicle:\n' + self.year + ' ' + self.make + ' ' + self.model + ' ' + self.trim
		



a = Vehicle('2017','Ford','Mustang','v6')
carss = Cars()
carss.addCar(a)
#print(cars)