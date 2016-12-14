import sys, histogram, random, math

def generateRandomWordFromHistogram(_histogram):
	totalWords = 0
	listOfTuples = []

	for word, count in _histogram.iteritems():
		# add word to tuple with it's range (being its upper bound)
		upperBound = totalWords + count
		listOfTuples.append((word, upperBound))
		totalWords += count

	# generate random int and then binary search to find the word it correlates to
	randomInt = random.randint(1, totalWords)
	word = binarySearch(listOfTuples, randomInt)
	return word

def binarySearch(tuples, val):
	# take out the tests and create own file
	# assert len(tuples) > 0
	midpointIndexOfTuplesList = len(tuples) // 2
	# assert midpointIndexOfTuplesList < len(tuples), "midpoint: " + str(midpointIndexOfTuplesList)
	if len(tuples) == 1:
		word = tuples[midpointIndexOfTuplesList][0]
		return word

	midpointOfTuplesList = tuples[midpointIndexOfTuplesList]
	
	lowerBoundOfMidpoint = tuples[midpointIndexOfTuplesList - 1][1]
	upperBoundOfMidpoint = midpointOfTuplesList[1]

	if lowerBoundOfMidpoint <= val <= upperBoundOfMidpoint:
		return tuples[midpointIndexOfTuplesList][0]
	elif val < lowerBoundOfMidpoint:
		upperBound = midpointIndexOfTuplesList - 1
		return binarySearch(tuples[:upperBound], val)
	elif upperBoundOfMidpoint < val:
		upperBound = midpointIndexOfTuplesList - 1
		return binarySearch(tuples[midpointIndexOfTuplesList:], val)



