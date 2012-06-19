#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
NLTK :D
"""
import nltk
import sys
import urllib

#have you passed all the parameters?
if (len(sys.argv) < 3):
     print "execution: " + sys.argv[0] + " number_of_words filename1 filename2 ..."
     print "example: " + sys.argv[0] + " 100 txt/*"
     quit()
     
rawText = "" #string with all the text from all the files passed
for currentFile in sys.argv[2:]:
    in_file = open(currentFile, "r")
    rawText += in_file.read()
    in_file.close()
myText = nltk.Text(nltk.word_tokenize(rawText))

#let's jam
print myText.generate(int(sys.argv[1]))
