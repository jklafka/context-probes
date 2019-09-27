import json
import sys
import csv

if __name__ == "__main__":
    filepath = sys.argv[1]
    glove_file = open(filepath, 'r')
    contents = [line.rstrip('\n') for line in glove_file]
    glove_dict = {}
    for pair in contents:
        word, vec = pair.split(' ', 1)
        glove_dict[word] = vec

    messages = []
    stimuli = sys.argv[2]
    with open("../data/" + stimuli, 'r') as data:
        csv_reader = csv.reader(data)
        for row in csv_reader:
            messages.append(row[0])
    vocab_list = []
    for message in messages:
        words = message.split()
        for word in words:
            if word.lower() not in vocab_list:
                vocab_list.append(word.lower())
    test = sys.argv[3]
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
    f = open("task_dict.json", 'w')
    f.write(json_file)
    f.close()
