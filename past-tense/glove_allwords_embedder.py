import json
import csv
import numpy as np

with open("task_dict.json", 'r') as json_file:
    vocab_dict = json.load(json_file)
for key, val in vocab_dict.items():
    vocab_dict[key] = [float(num) for num in val.split()]

## now for the train data
messages = []
labels = []
with open("../data/active_train.csv", 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        messages.append(row[0])
        labels.append(row[1])

word_embeddings = {0: [],
    1: [],
    2: [],
    3: [],
    4: []}
for message in messages:
    words = message.split()
    for i in range(len(words)):
        embedding = np.array(vocab_dict[words[i].lower()])
        word_embeddings[i].append(embedding)
for i in range(5):
    with open("../data/glove_word" + str(i) + "_train.csv", 'w') as dataset:
      csv_writer = csv.writer(dataset, delimiter = ',')
      for j in range(len(word_embeddings[i])):
          csv_writer.writerow(word_embeddings[i][j].tolist() + [labels[i]])

## now for the test data
messages = []
labels = []
with open("../data/active_test.csv", 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        messages.append(row[0])
        labels.append(row[1])

word_embeddings = {0: [],
    1: [],
    2: [],
    3: [],
    4: []}
for message in messages:
    words = message.split()
    for i in range(len(words)):
        embedding = np.array(vocab_dict[words[i].lower()])
        word_embeddings[i].append(embedding)
for i in range(5):
    with open("../data/glove_word" + str(i) + "_test.csv", 'w') as dataset:
      csv_writer = csv.writer(dataset, delimiter = ',')
      for j in range(len(word_embeddings[i])):
          csv_writer.writerow(word_embeddings[i][j].tolist() + [labels[i]])
