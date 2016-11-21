
import os
from os import path

import csv

import unicodedata
import codecs
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

from nltk.classify.naivebayes import NaiveBayesClassifier
from exceptions import UnicodeDecodeError


def unicode_normalization(file_path):

    source_file_name  = os.path.split(file_path)[1]
    target_dir = os.path.join(os.path.split(file_path)[0], 'encoded_data')

    source_file = codecs.open(file_path,mode = 'r',
                              encoding = 'latin-1', errors = 'ignore')
    target_file = codecs.open(os.path.join(target_dir,source_file_name),
                mode = 'w',
                encoding = 'utf-8',
                errors = 'ignore')
    while True:
        contents = source_file.read()
        if not contents:
            break
        target_file.write(contents)

def corpus_treatment(root):
    def check_encode_dir():
        if not os.path.exists(encoded_data_dir):
            os.makedirs(encoded_data_dir)
        return None

    corpus_dir = root
    encoded_data_dir = root + '/encoded_data'
    check_encode_dir()
    files = [f for f in os.listdir(corpus_dir)
                if path.isfile(path.join(corpus_dir,f))]

    for file in files:
        unicode_normalization(path.join(corpus_dir,file))

    return None

# fileids_ = corpus_dir + '/rt-polarity*'

corpus_dir =  '/home/mayank/IdeaProjects/Lab_Machine_Learning/src/Text_Analytics/data/rt-polaritydata'

cat_map_ = {
    'rt-polarity.pos' : ['pos'],
    'rt-polarity.neg' : ['neg']
}

corpus_treatment(corpus_dir)

encoded_corpus_dir = os.path.join(corpus_dir, 'encoded_data')
fileids_ = '^rt-polarity.*'

categorized_plaintext_corpusreader = CategorizedPlaintextCorpusReader(
    root = encoded_corpus_dir, cat_map = t_map_ , fileids = fileids_,
    )

pos_words = categorized_plaintext_corpusreader.words(categories=['pos'])
pos_sents = categorized_plaintext_corpusreader.sents(categories=['pos'])
pos_paras = categorized_plaintext_corpusreader.paras(categories=['pos'])

neg_words = categorized_plaintext_corpusreader.words(categories=['pos'])
neg_sents = categorized_plaintext_corpusreader.sents(categories=['neg'])
neg_paras = categorized_plaintext_corpusreader.paras(categories=['neg'])


# NOTE: para views are not working to be looked into later

# classification
train  = pos_words
classifier = NaiveBayesClassifier.train(train)