import json, csv, argparse

parser = argparse.ArgumentParser()
parser.add_argument("glove_dict", help="Dictionary mapping words to their GloVe vectors")
parser.add_argument("trainset", help="Training input sentences you want to embed plus labels")
parser.add_argument("testset", help="Testing input sentences you want to embed plus labels")
args = parser.parse_args()

filepath = args.glove_dict
glove_file = open(filepath, 'r')
contents = [line.rstrip('\n') for line in glove_file]
glove_dict = {}
for pair in contents:
    word, vec = pair.split(' ', 1)
    glove_dict[word] = vec

messages = []
train = args.trainset
with open("../data/" + train, 'r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        messages.append(row[0])
vocab_list = []
for message in messages:
    words = message.split()
    for word in words:
        if word.lower() not in vocab_list:
            vocab_list.append(word.lower())
            
test = args.testset
with open("../data/" + test, 'r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        messages.append(row[0])
for message in messages:
    words = message.split()
    for word in words:
        if word.lower() not in vocab_list:
            vocab_list.append(word.lower())

task_dict = {key:val for key, val in glove_dict.items() if key in vocab_list}
json_file = json.dumps(task_dict)
f = open("glove.json", 'w')
f.write(json_file)
f.close()
