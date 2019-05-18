from allennlp.modules.elmo import Elmo, batch_to_ids
import csv
import argparse

options_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_options.json"
weight_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"

# Compute two different representation for each token.
# Each representation is a linear weighted combination for the
# 3 layers in ELMo (i.e., charcnn, the outputs of the two BiLSTM))
elmo = Elmo(options_file, weight_file, 2, dropout=0)

# use batch_to_ids to convert sentences to character ids
# sentence = [['The', 'doctor', 'punched', 'the', 'scientist', '.']]
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
    character_ids = batch_to_ids(sentences[i])
    embeddings = elmo(character_ids)
    reps = embeddings["elmo_representations"]
    sen_embeddings.append(reps)
    verb_embeddings.append([reps[0][0, verb_indices[i], :], \
        reps[1][0, verb_indices[i], :]])


with open("data/elmo_sen_train.csv", 'w') as dataset:
  csv_writer = csv.writer(dataset, delimiter = ',')
  for i in range(len(sen_embeddings)):
      csv_writer.writerow(sen_embeddings[i].tolist() + [labels[i]])


with open("data/elmo_verb_train.csv", 'w') as dataset:
  csv_writer = csv.writer(dataset, delimiter = ',')
  for i in range(len(verb_embeddings)):
      csv_writer.writerow(verb_embeddings[i].tolist() + [labels[i]])


'''
Procedure: for each sentence, split it into words/punctuation.
batch_to_ids to convert the sentence into a format elmo can work with.
Then create the embeddings. You get a dictionary mapping 'elmo_representations'
    to a list of torch tensors, each of which is dim number of sentences x number
    of layers x number of dimensions of each representation
Create 6 output files: {combining the two reps; first rep; second rep} X
    {only the verb we care about; the entire sentence}
'''
