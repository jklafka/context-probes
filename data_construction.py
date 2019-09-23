import csv
import random

subjects = []

## number
with open("stimuli/number_nouns.csv", 'r') as f:
     reader = csv.reader(f)
     for line in reader:
         subjects.append((line[0], 0))
         subjects.append((line[1], 1))

## gender
with open("stimuli/gender_nouns.csv", 'r') as f:
     reader = csv.reader(f)
     for line in reader:
         subjects.append((line[0], int(line[1])))

verbs = open("stimuli/clean_verbs.txt", 'r').read().split()
trainVerbs = verbs[:80]
testVerbs = verbs[80:100]

## tense
# present_verbs = open("stimuli/present_verbs.txt", 'r').read().split()

## alternate nouns
alternates = []
with open("stimuli/other_nouns.csv", 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        alternates.append(line[0])

sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainSubjs:
            ## stuff goes here

random.shuffle(sens)
sens = sens[:4000]

with open("../data/quant_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))

sens = []

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for testObj in testSubjs:
            ## stuff goes here


random.shuffle(sens)
sens = sens[:1000]

with open("../data/quant_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
