import re

def removeTitleAndChapterLines(corpus):
	#  remove all lines that are written in all caps
	editedCorpus = re.sub(r"[A-Z]+\n", '', corpus)
	# re.sub("^[A-Z]+$", '')
	# remove all lines that begin with a number and have alphanumeric words following
	editedCorpus = re.sub(r"\d+. ?[\w ]+.?", '', editedCorpus)
	#  remove lines that have a number followed by a periods
	editedCorpus = re.sub(r"\d+. ?", '', editedCorpus)
	return editedCorpus

def removeNewLineCharsAtEndOfEachLine(corpus):
	# remove new lines
	return re.sub(r"\n", ' ', corpus)

def removeWhitespace(corpus):
	# # remove empty lines
	# corpus = re.sub("^\n$", '', corpus)

	# replace double spaces with single spaces
	editedCorpus = re.sub(r" {2,}", " ", corpus)
	# replace spaces before sentences begin on new lines -- not sure if this works 
	editedCorpus = re.sub(r"^( +)", "", editedCorpus)
	return editedCorpus

def removeTitles(corpus):
	# Mx? 
	# search for mr, mrs, etc for period removal
	editedCorpus = re.sub(r"[mMdD][rR][sS]?\.", "", corpus)
	editedCorpus = re.sub(r"[mMdD][xX]?\.", "", editedCorpus)
	return editedCorpus

def removePunctuation(corpus):
	#  remove commas, colons, dashes
	editedCorpus = re.sub(r"[;:_*?!|\{\}]+", "", corpus)
	# change dashes to spaces
	editedCorpus = re.sub("-", " ", editedCorpus)
	return editedCorpus

def removeFootnotes(corpus):
	# remove all digits in square brackets [footnotes]
	editedCorpus = re.sub(r"\[\d+\]", '', corpus)
	editedCorpus = re.sub(r"[\[\]]", '', editedCorpus)
	return editedCorpus

def handleAndComp(corpus):
	# remove &c
	editedCorpus = re.sub(r"(&c)\b\.", "", corpus)
	# replace & with and
	editedCorpus = re.sub("&", "and", editedCorpus)
	return editedCorpus

# should probably remove this 
def putEachSentenceOnANewLine(corpus):
	# split by . -- having a sentence per line
	return corpus.replace('.', '\n')

def cleanText(corpus):
	corpus = removeTitleAndChapterLines(corpus)
	corpus = removeNewLineCharsAtEndOfEachLine(corpus)
	corpus = removeTitles(corpus)
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
		file_ = open(filename)
		text =  file_.read()
		print cleanText(text)
	else:
		print('No source text filename given as argument')