from allennlp.commands.elmo import ElmoEmbedder
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("trainset", help="Training input sentences you want to embed plus labels")
parser.add_argument("testset", help="Testing input sentences you want to embed plus labels")
args = parser.parse_args()


#set up logging
import logging
logging.basicConfig(filename = "elmo.log", format="%(message)s", level=logging.INFO)

TOKENS = [0, 1, 2, 3, 4]
elmo = ElmoEmbedder(cuda_device = 0)

sentences = []
labels = []
probes = []
# verb_indices = []
with open(args.trainset, 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        split_sen = row[0].split()
        sentences.append(split_sen)
        labels.append(row[1])
        split_sen = row[2].split()
        probes.append(split_sen)

vocab = {word for item in sentences for word in item.split()} | {word for item in probes \
    for word in item.split()}
vocab_dict = {}
k = len(vocab)
for i, word in enumerate(vocab):
    onehot = [0] * k
    onehot[i] = 1
    vocab_dict[word] = onehot

word_embeddings = {0: [],
    1: [],
    2: [],
    3: [],
    4: []}
for j in range(len(sentences)):
    embeddings = elmo.embed_sentence(sentences[j])
    probe_word = sentences[j].split()[1]
    probe_vector = vocab_dict[probe_word]
    # probe_embeddings = elmo.embed_sentence(probes[j])
    for i in TOKENS:
        word_embeddings[TOKENS.index(i)].append(embeddings[1, i, :] + \
            # probe_embeddings[1, 1, :])
            probe_vector)

for i in range(5):
    with open("../../data/elmo/train" + str(i) + ".csv", 'w') as dataset:
      csv_writer = csv.writer(dataset, delimiter = ',')
      for j in range(len(word_embeddings[i])):
          csv_writer.writerow(word_embeddings[i][j].tolist() + [labels[j]])


sentences = []
labels = []
probes = []
# verb_indices = []
with open(args.testset, 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        split_sen = row[0].split()
        sentences.append(split_sen)
        labels.append(row[1])
        split_sen = row[2].split()
        probes.append(split_sen)

vocab = {word for item in sentences for word in item.split()} | {word for item in probes \
    for word in item.split()}
vocab_dict = {}
k = len(vocab)
for i, word in enumerate(vocab):
    onehot = [0] * k
    onehot[i] = 1
    vocab_dict[word] = onehot

word_embeddings = {0: [],
    1: [],
    2: [],
    3: [],
    4: []}
for j in range(len(sentences)):
    embeddings = elmo.embed_sentence(sentences[j])
    probe_word = sentences[j].split()[1]
    probe_vector = vocab_dict[probe_word]
    # probe_embeddings = elmo.embed_sentence(probes[j])
    for i in TOKENS:
        word_embeddings[TOKENS.index(i)].append(embeddings[1, i, :] + \
            # probe_embeddings[1, 1, :])
            probe_vector)

for i in range(5):
    with open("../../data/elmo/test" + str(i) + ".csv", 'w') as dataset:
      csv_writer = csv.writer(dataset, delimiter = ',')
      for j in range(len(word_embeddings[i])):
          csv_writer.writerow(word_embeddings[i][j].tolist() + [labels[j]])
