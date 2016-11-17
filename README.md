# README 

These scripts and folders of data were used in the **Intro to Text Analysis workshop** led by Robin Davis at John Jay College of Criminal Justice on November 16, 2016, sponsored by the [LACUNY Emerging Technologies Committee](http://commons.gc.cuny.edu/groups/lacuny-emerging-technologies-committee/). 

[Slides (on Google Docs)](https://docs.google.com/presentation/d/1IJLhIr17pO5iGt7qU8P0J84TekUFyaBALo4CJNlDn0g/edit?usp=sharing)

In this workshop, we looked at a brief history of humanities text analysis and covered the basics of using text as data. Then we explored [Voyant Tools](http://voyant-tools.org), [Google Books n-gram viewer](https://books.google.com/ngrams), and sentiment analysis. 

To use the Python scripts in this folder, you'll need to install: 
- Python 2.7 (2.7.3 is my personal fave) 
- IDLE (should come with Python) 
- [Numpy, a Python package](https://pypi.python.org/pypi/numpy)
- [NLTK, a Python package](http://www.nltk.org/install.html)

You'll also need to install NLTK modules. In Python: 
```
import nltk
nltk.download() 
```
A window should pop up. It might appear *behind* your current window. In the window, select the line beginning with **book** to download everything used in the book. It might take a while. 

**Not included in this repo**: ```pos_list.txt``` and ```neg_list.txt```, the lists of positive and negative words used in this repository. Were you at the workshop? Email Robin for the lists we used. Not at the workshop? Look online for lists of sentiment-bearing words. You'll have to run them through the PorterStemmer that comes with NLTK. Each word should be on its own line.

Note: You will probably run into some kind of errors with these scripts. That is the nature of running Python in different environments (and I haven't built in error-handling). If the errors are ignorable, then ignore them. If they won't let the script run at all, see if you can fix it by googling the error message. No luck? Sorry Charlie! I've included .txt files of sample output to see what you should have gotten.

## Further work 
Interested in learning more about Python-powered text analysis? Make your way through the [NLTK book](http://www.nltk.org/book/), freely available online and very engagingly written. It teaches you Python *and* natural language processing (NLP) at the same time, so you don't have to know Python to begin. 

## Data sources
- `data_novels/` - Project Gutenberg
- `data_sotu/` - Project Gutenberg (split up with Python); includes congressional addresses that aren't technically State of the Union addresses
- `data_columns/` - Handful of newspaper/magazine columns scraped from the open web
