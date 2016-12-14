import re

def removeRemainingPunctuation(text):
    # removes periods, commas, and parenthesis from corpus
    text = re.sub(r"[.,()\"']", "", text)
    return text

def splitOnWhitespace(text):
    return re.split('\s+', text)

def tokenize(text):
    cleanedText = removeRemainingPunctuation(text)
    tokens = splitOnWhitespace(cleanedText)
    return tokens

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open().read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename given as argument')