"""

"""

from corpora import Corpus
from nltk.corpus import PlaintextCorpusReader
import csv

corpus_path='/home/mayank/IdeaProjects/Lab_Machine_Learning/src/Text_Analytics/test'
Corpus.create(corpus_path)
corpus = Corpus(corpus_path)

training_file_path ="/home/mayank/IdeaProjects/Lab_Machine_Learning/src/resources/TrainingData.csv"
reader = csv.reader(open(training_file_path,'r'))

for (i,row) in enumerate(reader,1):
    print i
    corpus.add(row[6].decode('utf-8'),i)
    if i==10:break


print len(corpus)
print corpus.get()