
import os

import csv

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

corpus_dir =  '/home/mayank/IdeaProjects/Lab_Machine_Learning/src/Text_Analytics/data/rt-polaritydata'

cat_map_ = {
    'rt-polarity.pos' : ['pos'],
    'rt-polarity.neg' : ['neg']
}

# fileids_ = corpus_dir + '/rt-polarity*'

fileids_ = '^rt-polarity.*'

categorized_plaintext_corpusreader = CategorizedPlaintextCorpusReader(
    root = corpus_dir, cat_map = cat_map_ , fileids = fileids_)

print categorized_plaintext_corpusreader.categories()

pos_view = categorized_plaintext_corpusreader.words(categories='pos')