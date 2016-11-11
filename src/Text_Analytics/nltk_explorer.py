import os
import re
import csv

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader



srm_data_dir = '/home/mayank/work/projects/SRM/Data'

training_file_path = os.path.join(srm_data_dir, 'TrainingData.csv')
training_file = open(training_file_path, 'r')

root_dir = os.path.join(srm_data_dir, 'sub_data')


# noraml_reader = PlaintextCorpusReader(root = root_dir,
#                                       fileids = ['Financial.csv'])

cat_map_ ={
    'Compliance' : 'Compliance.csv',
    'Financial' : 'Financial.csv',
    'Operational' : 'Operational.csv',
    'Strategic' : 'Strategic.csv'
}

cat_reader = CategorizedPlaintextCorpusReader(root = root_dir,
                                              fileids = r'$.csv',
                                              cat_map = cat_map_)
