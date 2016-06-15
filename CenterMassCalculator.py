#Austin
#text file syntax "mass xcoord ycoord"
#LOOPS EVERYWHERE

import math

#open system text (contains coordinates and attributes)
#obviously replace pathway if needed
f = open("/Users/austinpeterson/Documents/Python/system.txt")
lines = f.readlines()[4:]#disregard instructions

lineCounter = 0

#strip newline characters from lines, count lines (not sure if useful)
for i, line in enumerate(lines):
	lines[i] = line.strip()
	lineCounter += 1

xCoordArray = []
yCoordArray = []
massArray = []

for i, line in enumerate(lines):
	#temp array to hold the 3 elements per line
	lineElements = lines[i].split()
	#have to use append to add elements to empty list
	#can't assign element to index that doesn't exist yet
	massArray.append(float(lineElements[0]))
	xCoordArray.append(float(lineElements[1]))
	yCoordArray.append(float(lineElements[2]))

#separate numerators for both axis of center mass
xNumeratorArray = []
yNumeratorArray = []

#add m*x and m*y elements to their respective arrays
for i, xCoord in enumerate(xCoordArray):
	xNumeratorArray.append(massArray[i]*xCoordArray[i])
	yNumeratorArray.append(massArray[i]*yCoordArray[i])

totalMass = sum(massArray)
xNumeratorTotal = sum(xNumeratorArray)
yNumeratorTotal = sum(yNumeratorArray)

centerMassXCoord = xNumeratorTotal/totalMass
centerMassYCoord = yNumeratorTotal/totalMass

#why cant I square a float?
fromOrigin = math.sqrt(centerMassXCoord*centerMassXCoord+centerMassYCoord*centerMassYCoord)

print("The coordinate of the center mass of the system is: ")
print("("+str(centerMassXCoord)+", "+str(centerMassYCoord)+")\n")
print("Then distance from the origin to the center mass is: "+str(fromOrigin)+"\n")









