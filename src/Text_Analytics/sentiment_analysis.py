
import os

import csv



from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

from nltk.classify.naivebayes import NaiveBayesClassifier
from exceptions import UnicodeDecodeError

corpus_dir =  '/home/mayank/IdeaProjects/Lab_Machine_Learning/src/Text_Analytics/data/rt-polaritydata'

cat_map_ = {
    'rt-polarity.pos' : ['pos'],
    'rt-polarity.neg' : ['neg']
}

# fileids_ = corpus_dir + '/rt-polarity*'

fileids_ = '^rt-polarity.*'

categorized_plaintext_corpusreader = CategorizedPlaintextCorpusReader(
    root = corpus_dir, cat_map = cat_map_ , fileids = fileids_,
    )


# pos_view = categorized_plaintext_corpusreader.words(categories='pos')



# classification
sents = categorized_plaintext_corpusreader.sents()

for steam_view in sents:
    steam_view.close()

for  senetence in sents:
    try:
        print senetence
    except UnicodeDecodeError:
        print 'error'

# classifier = NaiveBayesClassifier.train()