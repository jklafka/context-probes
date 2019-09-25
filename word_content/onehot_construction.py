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
trainSubjs = nouns[:80]
testSubjs = nouns[80:100]

# create train set
# for each combination of verb, subject and object, create a sentence
# half negative labels with random other vocab index, half positive (same) index
sens = []
counter = 0
for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
         for trainObj in trainSubjs:
            if trainObj != trainSubjs:
                # each stim has the form (sentence, vocab index, pos/neg label)
                if counter % 2 == 0: #positive labels
                    sens.append(("the " + trainSubj[0] + ' ' + trainVerb + " the " + trainObj[0], \
                        trainSubj[1], 1))
                else: # negative labels
                    label = random.randint(0, 100)
                    if label == trainSubj[1] or label == trainObj[1]:
                        label = random.randint(0, 100)
                    sens.append(("the " + trainSubj[0] + ' ' + trainVerb + " the " + trainObj[0], \
                        label, 0))
                counter += 1

random.shuffle(sens)
sens = sens[:4000]

with open("../data/onehot_subject_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))


# create test set
sens = []
counter = 0
for testVerb in testVerbs:
    for testSubj in testSubjs:
         for testObj in testSubjs:
            if testObj != testSubj:
                if counter % 2 == 0:
                    sens.append(("the " + testSubj[0] + ' ' + testVerb + " the " + testObj[0], \
                        testSubj[1], 1))
                else:
                    label = random.randint(0, 100)
                    if label == testSubj[1] or label == testObj[1]:
                        label = random.randint(0, 100)
                    sens.append(("the " + testSubj[0] + ' ' + testVerb + " the " + testObj[0], \
                        label, 0))
                counter += 1

random.shuffle(sens)
sens = sens[:1000]

with open("../data/onehot_subject_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
