from histogram import Histogram


def markovChain(tokens):
	histogram = {}
	currentState = 0
	nextState = 1

	for word in tokens: 
		# if the next state index is out of range of the list, return the histogram
		if nextState == len(tokens):
			return histogram
		# for each word, add the word that follows to its histogram
		try:
			if histogram[word]:
				# histogram already exists, add to it or update the value
				histogram[word].update([tokens[nextState]])
		except KeyError: 
			# create the histogram if it does not exist already
			histogram[word] = Histogram()
			histogram[word].update([tokens[nextState]])
		currentState += 1
		nextState += 1