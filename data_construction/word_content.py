import csv
import random

verbs = open("clean_verbs.txt", 'r').read().split()

trainVerbs = verbs[:80]

testVerbs = verbs[80:100]


trainSubjs = ['person', 'man', 'woman', 'linguist', 'priest', 'worker', 'actor', \
        'reporter', 'judge']
testSubjs = ['player', 'lackey', 'boss', 'kid', 'friend', 'savior', 'doctor']

trainObjs = ['partner', 'barista', 'mother']
testObjs = ['father', 'runner', 'soldier']

sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for probe in trainSubjs:
            for trainObj in trainObjs:
            # for trainAdj in trainAdjs:
            # if trainSubj[1] != trainObj[1]:
                if probe == trainSubj:
                    sens.append(("The " + trainSubj + ' ' + trainVerb + ' the ' + \
                        trainObj, 1, "The " + probe + ' ' + trainVerb + ' the ' + \
                            trainObj))
                else:
                    sens.append(("The " + trainSubj + ' ' + trainVerb + ' the ' + \
                        trainObj, 0, "The " + probe + ' ' + trainVerb + ' the ' + \
                            trainObj))
random.shuffle(sens)
sens = sens[:4000]

with open("../data/wc_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))

sens = []

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for probe in testSubjs:
            for testObj in testObjs:
            # for testAdj in testAdjs:
            # if testSubj[1] != testObj[1]:
                if probe == testSubj:
                    sens.append(("The " + testSubj + ' ' + testVerb + ' the ' \
                    + testObj, 1, "The " + probe + ' ' + testVerb + ' the ' \
                    + testObj))
                else:
                    sens.append(("The " + testSubj + ' ' + testVerb + ' the ' \
                    + testObj, 0, "The " + probe + ' ' + testVerb + ' the ' \
                    + testObj))
                # sens.append(("The " + testSubj[0] + ' ' + testVerb + ' the ' \
                # + testAdj + ' ' + testObj[0], testSubj[1]))


random.shuffle(sens)
sens = sens[:1000]

with open("../data/wc_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
