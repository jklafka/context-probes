import torch
from pytorch_pretrained_bert import OpenAIGPTTokenizer, OpenAIGPTModel

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("trainset", help="Training input sentences you want to embed plus labels")
parser.add_argument("testset", help="Testing input sentences you want to embed plus labels")
args = parser.parse_args()

#set up logging
import logging
logging.basicConfig(filename = "gpt.log", format="%(message)s", level=logging.INFO)

# Load pre-trained model tokenizer (vocabulary)
tokenizer = OpenAIGPTTokenizer.from_pretrained('openai-gpt')

# Load pre-trained model (weights)
model = OpenAIGPTModel.from_pretrained('openai-gpt')
model.to('cuda')
model.eval()



NUM_TRAIN = 4000
TOKENS = [0, 1, 2, 3, 4]
messages = []
labels = []
probes = []
with open(args.trainset, 'r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        messages.append(row[0])
        labels.append(row[1])
        probes.append(row[2])

with open(args.testset, 'r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        messages.append(row[0])
        labels.append(row[1])
        probes.append(row[2])

vocab = {word for item in messages for word in item.split()} | {word for item in probes \
    for word in item.split()}
vocab_dict = {}
k = len(vocab)
for i, word in enumerate(vocab):
    onehot = [0] * k
    onehot[i] = 1
    vocab_dict[word] = onehot

for j in range(len(messages)):
    text = messages[j]
    #tokenize input
    tokenized_text = tokenizer.tokenize(text)
    #if len(tokenized_text) != len(TOKENS):
    #    continue
    #convert to vocabulary indices tensor
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    tokens_tensor = torch.tensor([indexed_tokens])

    tokens_tensor = tokens_tensor.to('cuda')

    with torch.no_grad():
        hidden_states = model(tokens_tensor)
    # get list of the embeddings from the lowest layer - 0 index for lowest layer up to 4
    embeddings = [hidden_states[:, i, :] for i in TOKENS]


    # text = probes[j]
    # #tokenize input
    # tokenized_text = tokenizer.tokenize(text)
    # #if len(tokenized_text) != len(TOKENS):
    # #    continue
    # #convert to vocabulary indices tensor
    # indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    # tokens_tensor = torch.tensor([indexed_tokens])
    #
    # tokens_tensor = tokens_tensor.to('cuda')
    #
    # with torch.no_grad():
    #     hidden_states = model(tokens_tensor)
    # # get list of the embeddings from the lowest layer - 0 index for lowest layer up to 4
    # probe_embeddings = [hidden_states[:, i, :] for i in TOKENS]

    probe_word = text.split()[1]
    probe_vector = vocab_dict[probe_word]

    for i in range(len(TOKENS)):
        vector = embeddings[i].tolist()[0]
        probe_vector = probe_embeddings[1].tolist()[0] ####### CHANGE #######
        if j < NUM_TRAIN:
            with open("../../data/gpt/train" + str(i) + ".csv", 'a') as output:
                csv_writer = csv.writer(output)
                csv_writer.writerow(vector + probe_vector + [labels[j]])
        else:
            with open("../../data/gpt/test" + str(i) + ".csv", 'a') as output:
                csv_writer = csv.writer(output)
                csv_writer.writerow(vector + probe_vector + [labels[j]])
