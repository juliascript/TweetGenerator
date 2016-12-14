from clean_text import cleanText
from tokenize import tokenize
from markov import markovChain, randomWalk


# set up flask app with mongodb
# everytime text is cleaned and tokenized, throw into db, w it's respected range 
#   since the data is being stored in tuples with upper bounds, this is going to get 
#   complicated -- assignment of lower and upper bounds everytime a new corpus is added
# 

# cleaning text and tokenizing should not be run more than once
if __name__ == "__main__":
	import sys
	if len(sys.argv) > 2:
		filename = sys.argv[1]
		source = open(filename).read()	
		cleanedText = cleanText(source)
		tokens = tokenize(cleanedText)
		markov_ = markovChain(tokens)
		numOfSteps = int(sys.argv[2])
		sentence = randomWalk(numOfSteps, markov_)
		print(sentence)
	elif len(sys.argv) > 1:
		print('Number of words not specified')
	else:
		print('No source text filename given as argument')