
import os

import csv

import unicodedata
import codecs
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

from nltk.classify.naivebayes import NaiveBayesClassifier
from exceptions import UnicodeDecodeError

corpus_dir =  '/home/mayank/IdeaProjects/Lab_Machine_Learning/src/Text_Analytics/data/rt-polaritydata'

cat_map_ = {
    'rt-polarity.pos' : ['pos'],
    'rt-polarity.neg' : ['neg']
}

def unicode_normalization(file_path):
    source_file = codecs.open(file_path,mode = 'r',
                              encoding = 'latin-1', errors = 'ignore')
    target_file = codecs.open(file_path.rpartition('/')[0]
                + '/un_'
                + file_path.rpartition('/')[-1],
                mode = 'w',
                encoding = 'utf-8',
                errors = 'ignore')
    while True:
        contents = source_file.read()
        if not contents:
            break
        target_file.write(contents)

def corpus_treatment(root):

    corpus_dir = root

    files =
    return None

# fileids_ = corpus_dir + '/rt-polarity*'

fileids_ = '^rt-polarity.*'

categorized_plaintext_corpusreader = CategorizedPlaintextCorpusReader(
    root = corpus_dir, cat_map = cat_map_ , fileids = fileids_,
    )

pos_words = categorized_plaintext_corpusreader.words(categories=['pos'])
pos_sents = categorized_plaintext_corpusreader.sents(categories=['pos'])
pos_paras = categorized_plaintext_corpusreader.paras(categories=['pos'])

neg_words = categorized_plaintext_corpusreader.words(categories=['pos'])
neg_sents = categorized_plaintext_corpusreader.sents(categories=['neg'])
neg_paras = categorized_plaintext_corpusreader.paras(categories=['neg'])


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