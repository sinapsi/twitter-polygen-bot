import nltk
import sys
import urllib

rawText = ""
print "scaricato :O"
for currentFile in sys.argv[2:]:
    in_file = open(currentFile,"r")
    rawText += in_file.read()
    in_file.close()
myText = nltk.Text(nltk.word_tokenize(rawText))

print myText.generate(int(sys.argv[1])) 
