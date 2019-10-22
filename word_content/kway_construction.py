import csv
import random

verbs = open("../stimuli/clean_verbs.txt", 'r').read().split()
trainVerbs = verbs[:80]
testVerbs = verbs[80:100]

## tense
# present_verbs = open("stimuli/present_verbs.txt", 'r').read().split()

## nouns
nouns = []
with open("../stimuli/other_nouns.csv", 'r') as f:
    reader = csv.reader(f)
    for i, line in enumerate(reader):
        nouns.append([line[0], i]) #vocabulary index for one-hot vectors

# simulate train-test split
trainSubjs = nouns[:40]
testSubjs1 = nouns[80:100]
testSubjs2 = nouns[60:80]

# create train set: every train subject is paired with its vocabulary index
sens = []
for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
         for trainObj in testSubjs1:
            # if trainObj != trainSubjs:
                # each stim has the form (sentence, vocab index)
                sens.append(("the " + trainSubj[0] + ' ' + trainVerb + " the " + trainObj[0], \
                    trainSubj[1]))

random.shuffle(sens)
sens = sens[:4000]

with open("../data/kway_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))


# create test set
sens = []
for testVerb in testVerbs:
    for testSubj in trainSubjs:
         for testObj in testSubjs2:
            # if testObj != testSubj:
                # each stim has the form (sentence, vocab index)
                sens.append(("the " + testSubj[0] + ' ' + testVerb + " the " + testObj[0], \
                    testSubj[1]))


random.shuffle(sens)
sens = sens[:1000]

with open("../data/kway_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
