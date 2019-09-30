import csv
import random

nouns = []

# change this to which linguistic element you want to probe
output_name = "number"
# change the target for the noun tasks
target_name = "subject"

num_train = 80
num_test = 100

## number
if output_name == "number":
    with open("stimuli/number_nouns.csv", 'r') as f:
         reader = csv.reader(f)
         for line in reader:
             nouns.append((line[0], 0))
             nouns.append((line[1], 1))

## gender
if output_name == "gender":
    with open("stimuli/gender_nouns.csv", 'r') as f:
         reader = csv.reader(f)
         for line in reader:
             nouns.append((line[0], int(line[1])))
             num_train = 30
             num_test = 40

verbs = open("stimuli/clean_verbs.txt", 'r').read().split()

## tense
if output_name == "tense":
    present_verbs = open("stimuli/present_verbs.txt", 'r').read().split()
    trainVerbs = list(zip(verbs[:40], [1] * 40)) + \
        list(zip(present_verbs[:40], [0] * 40))
    testVerbs = list(zip(verbs[81:90], [1] * 10)) + \
        list(zip(present_verbs[81:90], [0] * 10))
    # get subjects and objects
    with open("stimuli/other_nouns.csv", 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            nouns.append((line[0],'a'))

else:
    trainVerbs = list(zip(verbs[:80], ['a']*80))
    testVerbs = list(zip(verbs[80:100], ['a']*80))

# create train/test split with subjects
trainSubjs = nouns[:num_train+1]
testSubjs = nouns[num_train+1:num_test]


sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainSubjs:
            if trainObj != trainSubj:
                if output_name == "tense":
                    target = trainVerb
                else:
                    if target_name == "subject":
                        target = trainSubj
                    elif target_name == "object":
                        target = trainObj
                    else:
                        break
                sens.append(("the " + trainSubj[0] + ' ' + trainVerb[0] + " the " + \
                    trainObj[0], target[1]))

random.shuffle(sens)
sens = sens[:4000]

with open("data/" + target_name + '_' + output_name + "_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))

sens = []

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for testObj in testSubjs:
            if testObj != testSubj:
                if output_name == "tense":
                    target = testVerb
                else:
                    if target_name == "subject":
                        target = testSubj
                    elif target_name == "object":
                        target = testObj
                    else:
                        break
                sens.append(("the " + testSubj[0] + ' ' + testVerb[0] + " the " + \
                    testObj[0], target[1]))


random.shuffle(sens)
sens = sens[:1000]

with open("data/" + target_name + '_' + output_name + "_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
