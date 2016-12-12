import re

def removeTitleAndChapterLines(corpus):
	#  remove all lines that are written in all caps
	corpus = re.sub("[A-Z]+\n", '', corpus)
	# re.sub("^[A-Z]+$", '')
	# remove all lines that begin with a number and have alphanumeric words following
	corpus = re.sub("\d+. ?[\w ]+.?", '', corpus)
	#  remove lines that have a number followed by a periods
	corpus = re.sub("\d+. ?", '', corpus)
	return corpus

def removeNewLineCharsAtEndOfEachLine(corpus):
	# remove new lines
	corpus = re.sub("\n", ' ', corpus)
	return corpus

def removeWhitespace(corpus):
	# # remove empty lines
	# corpus = re.sub("^\n$", '', corpus)

	# replace double spaces with single spaces
	corpus = re.sub ("  ", " ", corpus)
	# replace spaces before sentences begin on new lines -- not sure if this works 
	corpus = re.sub("^( +)", "", corpus)
	return corpus

def removeMrMrs(corpus):
	# search for mr, mrs, etc for period removal
	corpus = re.sub("[mM][rR][sS]?.", "", corpus)
	return corpus

def removePunctuation(corpus):
	#  remove commas, colons, dashes
	corpus = re.sub("[;:_*\?!]+", "", corpus)
	# change dashes to spaces
	corpus = re.sub("-", " ", corpus)
	return corpus

def removeFootnotes(corpus):
	# remove all digits in square brackets [footnotes]
	corpus = re.sub("\[\d+\]", '', corpus)
	corpus = re.sub("[\[\]]", '', corpus)
	return corpus

def handleAndComp(corpus):
	# remove &c
	corpus = re.sub("(&c)\b.", "", corpus)
	# replace & with and
	corpus = re.sub("&", "and", corpus)
	return corpus

def putEachSentenceOnANewLine(corpus):
	# split by . -- having a sentence per line
	corpus = corpus.replace('.', '\n')
	return corpus

def clean_text(corpus):
	corpus = removeTitleAndChapterLines(corpus)
	corpus = removeNewLineCharsAtEndOfEachLine(corpus)
	corpus = removeMrMrs(corpus)
	corpus = removePunctuation(corpus)
	corpus = removeWhitespace(corpus)
	corpus = removeFootnotes(corpus)
	corpus = handleAndComp(corpus)
	corpus = putEachSentenceOnANewLine(corpus)
	return corpus

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		f = open(filename)
		f =  f.read()
		print clean_text(f)
	else:
		print('No source text filename given as argument')