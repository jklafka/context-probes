import csv
import random

verbs = open("clean_verbs.txt", 'r').read().split()

trainVerbs = verbs[:80]

testVerbs = verbs[80:100]

trainSubjs = [('person', 0), ('people', 1), ('man', 0), ('men', 1),
    ('woman', 0), ('women', 1), ("linguist", 0), ("linguists", 1), \
    ('priest', 0), ('priests', 1), ('soldiers', 1), ('worker', 0), \
    ('workers', 1), ('actor', 0), ('actors', 1), ('reporter', 0), ('reporters', 1), \
    ('judge', 0), ('judges', 1), ('player', 0)]

# ('Mouse', 0), , ('Players', 1)

testSubjs = [('lackey', 0), ('lackeys', 1), ('boss', 0), \
    ('bosses', 1), ('kid', 0), ('kids', 1), ('friend', 0), \
    ('friends', 1), ('savior', 0), ('saviors', 1), ('doctor', 0), ('doctors', 1)]

trainAdjs = ["friendly", "helpful", "old", "young", "new"]
testAdjs = ["good", "bad", "angry", "strange", "normal"]

sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainSubjs:
            for trainAdj in trainAdjs:
            # if trainSubj[1] != trainObj[1]:
                sens.append(("The " + trainSubj[0] + ' ' + trainVerb + ' the ' + \
                trainObj[0], trainSubj[1]))
                sens.append(("The " + trainSubj[0] + ' ' + trainVerb + ' the ' + \
                trainAdj + ' ' + trainObj[0], trainSubj[1]))
random.shuffle(sens)
sens = sens[:4000]

with open("../data/distance_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))

sens = []

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for testObj in testSubjs:
            for testAdj in testAdjs:
            # if testSubj[1] != testObj[1]:
                # sens.append(("The " + testSubj[0] + ' ' + testVerb + ' the ' \
                # + testObj[0], testSubj[1]))
                sens.append(("The " + testSubj[0] + ' ' + testVerb + ' the ' \
                + testAdj + ' ' + testObj[0], testSubj[1]))

random.shuffle(sens)
sens = sens[:1000]

with open("../data/distance_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
