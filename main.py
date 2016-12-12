import clean_text, tokenize, markov

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		source = open(filename).read()	
		cleanedText = clean_text.clean_text(source)
		tokens = tokenize.tokenize(cleanedText)
		markov = markov.markovChain(tokens)
		print(markov)
	else:
		print('No source text filename given as argument')