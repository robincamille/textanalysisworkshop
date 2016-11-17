# -*- coding: utf-8 -*-

##This script outputs the top 10 person names from the text using the
##Stanford Named Entity Recognition interface in NLTK.
##
##Caveats: first/last names and most honorifics not considered

from nltk import tree
from nltk import word_tokenize as tok
from nltk import pos_tag as postag
from nltk import ne_chunk as ne
from collections import Counter

infile = open('data_columns/nussbaum/nuss01.txt','r') # Put your filename here
source = infile.read()
source = source.decode('utf-8')
infile.close()

print 'Tokenizing'
sourcetok = tok(source)

print 'Tagging Part Of Speech (POS)...'
sourcetag = postag(sourcetok)

print 'Running POS-tagged text through Named Entity chunker...'
sourcene = ne(sourcetag, binary=False)

# Find just the Named Entities that we want
charsall = []
for n in sourcene:
    if type(n) == tree.Tree:
        #if n.label() == 'PERSON':
        
        if n.node == 'PERSON': #Options: PERSON, ORGANIZATION, LOCATION
            for m in n:
                charsall.append(m[0])

# Exclude honorifics
honorifics = ['Mr.', 'Mrs.', 'Ms.', 'Miss', 'Dr.', 'Prof.', 'Professor', 'Lord', 'Lady', 'Sir', 'Madam', 'Dame', 'Rev.', 'Rabbi']
charsallnames = []
for s in charsall:
    if s in honorifics:
        pass
    else:
        charsallnames.append(s)

# Find most common
counted = (word for word in charsallnames if word[:1].isupper())
c = Counter(counted)
charscommon = c.most_common(10)
chars = []
for s in charscommon:
    chars.append(s[0])

# Output
print '\nMost common names:'
for c in chars:
    print c
