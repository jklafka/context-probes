import csv
import random

verbs = open("clean_verbs.txt", 'r').read().split()

trainVerbs = verbs[:80]

testVerbs = verbs[80:100]


trainSubjs = [('person', 'man'), ('woman', 'linguist'), ('priest', 'worker'), ('actor', \
        'reporter'), ('judge', 'author')]
testSubjs = [('player', 'lackey'), ('boss', 'kid'), ('friend', 'savior'), ('doctor', 'lawyer')]


trainObjs = ['partner', 'barista', 'mother']
testObjs = ['father', 'runner', 'soldier']

sens = []
counter = 0
for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainObjs:
            for i in range(2):
                for r in range(2):
                    s = i
                    if r == 1:
                        s = 1-i
                    sens.append(("The " + trainSubj[i] + ' ' + trainVerb + ' the ' + \
                        trainObj, r, "The " + trainSubj[s]+ ' ' + trainVerb + ' the ' + \
                        trainObj))

random.shuffle(sens)
sens = sens[:4000]

with open("../data/wc_subject_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))

sens = []

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for testObj in testObjs:
            for i in range(2):
                for r in range(2):
                    s = i
                    if r == 1:
                        s = 1-i
                    sens.append(("The " + testSubj[i] + ' ' + testVerb + ' the ' \
                        + testObj, r, "The " + testSubj[s] + ' ' + testVerb + ' the ' \
                        + testObj))



random.shuffle(sens)
sens = sens[:1000]

with open("../data/wc_subject_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
