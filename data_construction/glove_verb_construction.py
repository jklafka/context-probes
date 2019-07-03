import csv
import random

verbs = []

with open("data/all_verbs.csv", 'r') as f:
     csv_reader = csv.reader(f)
     for row in csv_reader:
         verbs.append(row[0])
verbs = verbs[1:]

trainVerbs = verbs[:40]

testVerbs = verbs[41:50]

trainSubjs = [('Person', 0), ('People', 1), ('Man', 0), ('Men', 1),
    ('Woman', 0), ('Women', 1), ("Linguist", 0), ("Linguists", 1), \
    ('Goose', 0), ('Geese', 1), ('Mouse', 0), ('Mice', 1), ('Ox', 0), \
    ('Oxen', 1), ('Actor', 0), ('Actors', 1), ('Narwhal', 0), ('Narwhals', 1), \
    ('Judge', 0), ('Judges', 1), ('Player', 0), ('Players', 1)]

testSubjs = [('Dog', 0), ('Dogs', 1), ('Cat', 0), \
    ('Cats', 1), ('Bird', 0), ('Birds', 1), ('Friend', 0), ('Friends', 1), \
    ('Savior', 0), ('Saviors', 1), ('Doctor', 0), ('Doctors', 1)]

train_sens = []
test_sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        train_sens.append((trainVerb, trainSubj[1]))

for testVerb in testVerbs:
    for testSubj in testSubjs:
        test_sens.append((testVerb, testSubj[1]))

random.shuffle(train_sens)
random.shuffle(test_sens)

with open("data/glove_verb_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in train_sens:
         data_writer.writerow(list(row))

with open("data/glove_verb_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in test_sens:
         data_writer.writerow(list(row))
