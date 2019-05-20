from allennlp.commands.elmo import ElmoEmbedder
import csv
import argparse
import numpy as np

elmo = ElmoEmbedder()

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()
input_filename = args.input

sentences = []
labels = []
verb_indices = []
with open("data/" + input_filename, 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        split_sen = row[0].split()
        sentences.append(split_sen)
        labels.append(row[1])
        verb_indices.append(split_sen.index(row[2]))

sen_embeddings = []
verb_embeddings = []
for i in range(len(sentences)):
    sen_embedding = np.zeros(1024)
    embeddings = elmo.embed_sentence(sentences[i])
    n = embeddings.shape[1]
    for j in range(n):
        sen_embedding += embeddings[1, j, :]
    sen_embedding /= n
    sen_embeddings.append(sen_embedding)
    verb_embeddings.append(embeddings[1, verb_indices[i], :])


with open("data/elmo_sen_test.csv", 'w') as dataset:
  csv_writer = csv.writer(dataset, delimiter = ',')
  for i in range(len(sen_embeddings)):
      csv_writer.writerow(sen_embeddings[i].tolist() + [labels[i]])


with open("data/elmo_verb_test.csv", 'w') as dataset:
  csv_writer = csv.writer(dataset, delimiter = ',')
  for i in range(len(verb_embeddings)):
      csv_writer.writerow(verb_embeddings[i].tolist() + [labels[i]])


'''
I'm working with only the lower layer of the contexual word embeddings produced
    by ELMo, the one that is supposed to track syntax more closely.
'''
