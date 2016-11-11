import os

import csv

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

def read_file():
    for (row_no, line) in enumerate(reader,1):
        print 'row_number;%s' %(row_no)
        print line
        if row_no==5:
            break

def get_categories():
    cats=set()
    for (row_no, line) in enumerate(reader,1):
        cats.add(line[7])
    for junk in ['','Risk_Type']: cats.remove(junk)
    training_file.seek(0)
    return cats

def divide_data(cats):
    file_names={}
    for cat in cats:
        file_dir = os.path.join(srm_data_dir, 'sub_data')
        file_name=os.path.join(file_dir, cat + '.csv')
        file = open(file_name, 'w+')
        file_names[cat] = csv.writer(file)
    for (row_no, line) in enumerate(reader,1):
        cat = line[7]
        if file_names.has_key(cat):
            file_names[cat].writerow(line)
    training_file.seek(0)
    return None


srm_data_dir = '/home/mayank/work/projects/SRM/Data'

training_file_path = os.path.join(srm_data_dir, 'TrainingData.csv')
training_file = open(training_file_path, 'r')

reader = csv.reader(training_file)

cats = get_categories()
divide_data(cats)

root_dir = os.path.join(srm_data_dir, 'sub_data')

cat_reader = CategorizedCorpusReader()

noraml_reader = PlaintextCorpusReader(root = root_dir,
                                      fileids = ['Financial.csv'])

cat_reader = CategorizedCorpusReader(root = root_dir)
