# This script counts up positive and negative words in a
# text file. Scroll to bottom for the action!

# YOU WILL NEED TO HAVE A POS_LIST.TXT AND NEG_LIST.TXT FILE
# NOT INCLUDED IN THIS REPO
# Were you at the workshop? Email Robin for the lists we used.

import string, os
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# Open up lists of neg / pos words
filename = open('pos_list.txt','r')
positivesraw = filename.readlines()
filename.close()
positives = [w[:-1] for w in positivesraw]

filename = open('neg_list.txt','r')
negativesraw = filename.readlines()
filename.close()
negatives = [w[:-1] for w in negativesraw]


def sentanalysis(source):
    # Check every word in the source text against neg / pos lists
    #source = source.decode('utf-8') #uncomment if you get an ascii error
    source = source.split()
    sourcepos = []
    sourceneg = []
    for word in source:
        wordstem = ps.stem(word.strip(string.punctuation).lower()) # Stem word
        if wordstem in positives:
            sourcepos.append(wordstem)
        if wordstem in negatives:
            sourceneg.append(wordstem)

    # Score: positive words / all sentiment words
    allsentcount = len(sourcepos) + len(sourceneg)
    if allsentcount == 0:
        posscore = 0
        negscore = 0
    else:
        posscore = len(sourcepos) / float(allsentcount)
        negscore = len(sourceneg) / float(allsentcount)

    print "Positive score\t%.2f" % posscore
    print "Negative score\t%.2f" % negscore

    #print sourcepos # Uncomment me to see the positive words in your text
    #print sourceneg # Uncomment me to see the negative words in your text



# Open up the DOCUMENT you want to analyze
##filename = open('data_columns/dowd/dowd01.txt','r')
##text = filename.read()
##filename.close()
##sentanalysis(text)


# Open up a CORPUS you want to analyze
foldername = 'data_chats/'
for f in os.listdir(foldername)[1:15]:
    fl = open(foldername + f,'r')
    text = fl.read()
    fl.close()
    print f
    sentanalysis(text)
    print


# Tasks:
# 0. Run this with 50 library chats. Any especially good chats? Bad?
# 1. Comment out the corpus code, uncomment the document code.
#    Run this with the document of your choice.
# 2. Uncomment the last two lines of the sentanalysis function to see
#    the sentiment-bearing words for each text. (Do this with one
#    document, or just a few library chats.)
