import csv, argparse, zipfile

parser = argparse.ArgumentParser()
# parser.add_argument("glove", help="Text file mapping words to their GloVe vectors")
parser.add_argument("trainset", help="Training input sentences you want to embed plus labels")
parser.add_argument("testset", help="Testing input sentences you want to embed plus labels")
args = parser.parse_args()

# take in the GloVe dictionary: this is our embedder
filepath = "../embedders/glove/glove.txt" # args.glove
glove_file = open(filepath, 'r')
contents = [line.rstrip('\n') for line in glove_file]
glove_dict = {}
for pair in contents:
    word, vec = pair.split(' ', 1)
    glove_dict[word] = vec

# set parameters
NUM_TRAIN = 4000
INDICES = [0, 1, 5, 6, -1]
TOKENS = [0, 1, 2, 3, 4]
messages = []
labels = []

# read in training data
train_filename = args.trainset
with open(train_filename, 'r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        messages.append(row[0])
        labels.append(row[1])

# read in testing data
test_filename = args.testset
with open(test_filename, 'r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        messages.append(row[0])
        labels.append(row[1])

for j, message in enumerate(messages):
    words = message.split()
    embeddings = [glove_dict[word] for word in words]
    for i in TOKENS:
        vector = embeddings[INDICES[i]].split()
        if j < NUM_TRAIN:
            with open("../data/glove/train" + str(i) + ".csv", 'a') as output:
                csv_writer = csv.writer(output)
                csv_writer.writerow(vector + [labels[j]])
        else:
            with open("../data/glove/test" + str(i) + ".csv", 'a') as output:
                csv_writer = csv.writer(output)
                csv_writer.writerow(vector + [labels[j]])
