import os
import csv

data_dir='/home/mayank/work/projects/text_analytics/data_files'
nexis_data_dir='/home/mayank/work/projects/SRM/Data'
m_and_a=os.listdir(data_dir + '/merger_aquisitions')

training_file_path = nexis_data_dir + '/TrainingData.csv'

print m_and_a[1]

file = m_and_a[1]



def doc_extracter(file_path):
    f = open(file_path, 'r'):
    for
    return

file = open(training_file_path,'r')
reader = csv.reader(file)
