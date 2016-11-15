
import os

import csv

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

corpus_dir =  '/home/mayank/IdeaProjects/Lab_Machine_Learning/src/Text_Analytics/data/rt-polaritydata'

cat_map_ = {
    'pos' : 'rt-polarity.pos',
    'neg' : 'rt-polarity.neg'
}

fileids_ = []


categorized_plaintext_corpusreader = CategorizedPlaintextCorpusReader(
    root = corpus_dir, cat_map = cat_map_ , fileids = '*')