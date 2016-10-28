from nltk.book import *
from nltk import bigrams

#conetxt handling ######################
# will list all the contexts
text1.concordance('healthy')
#will list all the words that share a context
text1.similar('healthy')
#will list common contexts
text1.common_contexts(['healthy','poor'])



#length of text
len(text1)
#vocabulary of text
set(text1)
sorted(set(text1))
len(set(text3))

#lexical richness/diversity ; higher the number lower is the diversity
print len(text3)/len(set(text3))

#word count
text3.count('smote')
text1.count('whale')
#word %
100 * text3.count('a')/len(text3)
100 * text5.count('lol')/len(text5)

#draws the dispersion plots
text4.dispersion_plot(['citizens','democracy','freedon','duties','America'])
text1.dispersion_plot(['whale'])

#frequecy distributions
fdist1 = FreqDist(text1)
fdist1
vocab1 = fdist1.keys()
vocab1[:50]
fdist1['whale']
fdist1.plot(50, cumulative=True)

#finding long words - no count check
V = set(text1)
long_words = [w for w in V if len(w) > 15]
print sorted(long_words)
#finding long words - with
print sorted([w for w in set(text1) if len(w) > 7 and fdist1[w] > 7])

#FreqDist ##########################
# stores the number of times an observation has occurred
print FreqDist.__doc__

#retrurns the element with maximum value

fdist1.max()

print FreqDist.plot.__doc__

#collocations and bigrams
# d? biagram - pairs of words that occur in a sentence
b = bigrams(['more', 'is', 'said', 'than', 'done'])
# d? collocations: frequent bigrams with rare words. Stop words are ignored
print text4.collocations.__doc__
text4.collocations()
print text4.findall('States')


#analysing lengthif each word
fdist = FreqDist([len(w) for w in text1])
print fdist.max()
print fdist.freq(3)


# Corpora and Lexical Resources ########################

# Gutenberg Corpus
import nltk
print nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
type(emma)
help(gutenberg)
help(nltk.corpus.reader.plaintext.PlaintextCorpusReader)
help(nltk.corpus.reader.api.CorpusReader)

#brown corpus
from nltk.corpus import brown
brown.categories()