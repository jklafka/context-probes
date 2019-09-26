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

NUM_TRAIN = 4000
TOKENS = [0, 1, 2, 3, 4]
elmo = ElmoEmbedder(cuda_device = 0)

sentences = []
labels = []
probes = []

# read in training and testing data
with open(args.trainset, 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        split_sen = row[0].split()
        sentences.append(split_sen)
        probes.append(row[1])
        labels.append(row[2])

with open(args.testset, 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        split_sen = row[0].split()
        sentences.append(split_sen)
        probes.append(row[1])
        labels.append(row[2])


for j in range(len(sentences)):
    embeddings = elmo.embed_sentence(sentences[j])
    # make onehot vector
    probe_vector = [0] * 100
    probe_vector[int(probes[j]) - 1] = 1

    for i in TOKENS:
        vector = embeddings[1, i, :].tolist()

        if j < NUM_TRAIN:
            with open("../../data/elmo/train" + str(i) + ".csv", 'a') as output:
                csv_writer = csv.writer(output)
                csv_writer.writerow(vector + probe_vector + [labels[j]])
        else:
            with open("../../data/elmo/test" + str(i) + ".csv", 'a') as output:
                csv_writer = csv.writer(output)
                csv_writer.writerow(vector + probe_vector + [labels[j]])
