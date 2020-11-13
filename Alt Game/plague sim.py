import console, time, math, random
console.clear()
debug = False

#__________________________________________
#--------------World Info------------------
population = 7124543962 #7,124,543,962

infected = 2
healthy = population
dead = 0

#__________________________________________
#-------------Plague Info------------------
plagueType = 'virus'
plagueInfectivity = 0.01
infectivityPercent = plagueInfectivity*100




#__________________________________________
#-----------Logistic Information-----------
tick = 0
gameRunning = True


#__________________________________________


while gameRunning:
	time.sleep(1)
	console.clear()
	
	
	newInfect = random.randint(infectivityPercent, infected/2)
	healthy = population - infected
	infected += newInfect
	
	tick += 1
	
	print 'Plague Type:	' + plagueType
	print 'Infectivity:	'	+	str(infectivityPercent)
	print 'Test: '+ str(random.randint(0,infectivityPercent))
	print
	print 'Alive	: '+str(population)
	print 'Dead	: '+str(dead)
	print
	print 'Healthy: '+str(healthy)
	print 'Infected: ' + str(infected)
	print
	print 'Time: ' + str(tick)
	if healthy <= 0:
		gameRunning = False





if(debug):
	
	print ' -------------'
	print '|Population	:	' + str(population)
	print ' -------------'
	print '|Healthy		:	' +str(healthy)
	print '|Infected		:	' +str(infected)
	print ' -------------'