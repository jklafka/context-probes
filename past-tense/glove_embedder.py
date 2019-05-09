import json
import csv
import argparse
import numpy as np

with open("task_vocab.json", 'r') as json_file:
    vocab_dict = json.load(json_file)

parser = argparse.ArgumentParser()
parser.add_argument("data")
parser.add_argument("output")
args = parser.parse_args()
dataname = args.data
output_filename = args.output

sentences = []
messages = []
with open("data/" + dataname, 'r') as simple_data:
    csv_reader = csv.reader(simple_data)
    for row in csv_reader:
        sentences.append((row[0], row[1]))
        messages.append((row[0]))

message_embeddings = []
for message in messages:
    embedding = np.zeros(300)
    num = 0
    for word in message.split():
        embedding += np.array(vocab_dict[word.lower()])
        num += 1
    embedding /= num
    message_embeddings.append(embedding)

with open("data/" + output_filename, 'w') as dataset:
  csv_writer = csv.writer(dataset, delimiter = ',')
  for message_embedding in message_embeddings:
      csv_writer.writerow(message_embedding.tolist() + [sentences[i][1]])
