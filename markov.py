import random, weightedWordGenerator
from histogram import Histogram

def markovChain(tokens):
	histograms = {}
	currentState = 0
	nextState = 1

	for word in tokens: 
		# if the next state index is out of range of the list, return the histogram
		if nextState == len(tokens):
			return histograms
		# for each word, add the word that follows to its histogram
		try:
			if histograms[word]:
				# histogram already exists, add to it or update the value
				histograms[word].update([tokens[nextState]])
		except KeyError: 
			# create the histogram if it does not exist already
			histograms[word] = Histogram()
			histograms[word].update([tokens[nextState]])
		currentState += 1
		nextState += 1

def randomWalk(steps, markovChain):
	sentence = []
	# choose random word
	startWord = random.choice(markovChain.keys())
	# histogramForStartWord = markovChain[startWord]
	currentWord = startWord
	sentence.append(startWord)
	for i in range(steps):
		# find the histogram of the word
		histogramForWord = markovChain[currentWord]
		# calculate next word based on probablity 
		nextWord = weightedWordGenerator.generateRandomWordFromHistogram(histogramForWord)
		# add word to sentence
		sentence.append(nextWord)
		# then loop continues, set up for next loop
		currentWord = nextWord
	return (' ').join(sentence)


