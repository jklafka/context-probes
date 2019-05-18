import json
import csv
import argparse
import numpy as np

with open("task_vocab.json", 'r') as json_file:
    vocab_dict = json.load(json_file)
for key, val in vocab_dict.items():
    vocab_dict[key] = [float(num) for num in val.split()]

parser = argparse.ArgumentParser()
parser.add_argument("data")
parser.add_argument("output")
args = parser.parse_args()
input_filename = args.data
output_filename = args.output

verbs = []
labels = []
with open("data/" + input_filename, 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        verbs.append(row[0])
        labels.append(row[1])

verb_embeddings = []
for verb in verbs:
    embedding = np.array(vocab_dict[verb.lower()])
    verb_embeddings.append(embedding)

with open("data/" + output_filename, 'w') as dataset:
  csv_writer = csv.writer(dataset, delimiter = ',')
  for i in range(len(verb_embeddings)):
      csv_writer.writerow(verb_embeddings[i].tolist() + [labels[i]])
