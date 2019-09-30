import json, csv, argparse

parser = argparse.ArgumentParser()
parser.add_argument("glove_dict", help="Dictionary mapping words to their GloVe vectors")
parser.add_argument("trainset", help="Training input sentences you want to embed plus labels")
parser.add_argument("testset", help="Testing input sentences you want to embed plus labels")
args = parser.parse_args()

# take in the GloVe dictionary: this is our embedder
filepath = args.glove_dict
glove_file = open(filepath, 'r')
contents = [line.rstrip('\n') for line in glove_file]
glove_dict = {}
for pair in contents:
    word, vec = pair.split(' ', 1)
    glove_dict[word] = vec

NUM_TRAIN = 4000
TOKENS = [0, 1, 2, 3, 4]
messages = []
labels = []


train_filename = args.trainset
with open("../data/" + train_filename, 'r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        messages.append(row[0])
        labels.append(row[1])

test_filename = args.testset
with open("../data/" + test_filename, 'r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        messages.append(row[0])
        labels.append(row[1])

for j, message in enumerate(messages):
    words = message.split()
    embeddings = [glove_dict[word] for word in words]
    for i in TOKENS:
        vector = embeddings[i]
        if j < NUM_TRAIN:
            with open("../data/glove/train" + str(i) + ".csv", 'a') as output:
                csv_writer = csv.writer(output)
                csv_writer.writerow(vector + [labels[j]])
        else:
            with open("../data/glove/test" + str(i) + ".csv", 'a') as output:
                csv_writer = csv.writer(output)
                csv_writer.writerow(vector + [labels[j]])
