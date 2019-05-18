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

trainSubjs = [('person', 0), ('people', 1), ('man', 0), ('men', 1),
    ('woman', 0), ('women', 1), ("linguist", 0), ("linguists", 1), \
    ('goose', 0), ('geese', 1), ('mouse', 0), ('mice', 1), ('ox', 0), \
    ('oxen', 1), ('actor', 0), ('actors', 1), ('narwhal', 0), ('narwhals', 1), \
    ('judge', 0), ('judges', 1), ('player', 0), ('players', 1)]

testSubjs = [('dog', 0), ('dogs', 1), ('cat', 0), \
    ('cats', 1), ('bird', 0), ('birds', 1), ('friend', 0), ('friends', 1), \
    ('savior', 0), ('saviors', 1), ('doctor', 0), ('doctors', 1)]


subjectRCs = ["The {} that I wanted", "The {} that we wanted", \
    "The {} that they liked", "The {} that he wanted"]

objectRCs = ["that she created", "that they created", \
    "that I found", "that we found"]

itClefts = ["It was the {} that"]

negAdjuncts = ["but not the {}", "without the {}"]

embedClauses = ["that we found", "that I found", "that she created", \
    "that they created"]

Adjuncts = ["in my house", "with my father", "with my fathers", "in our house"]

train_sens = []
test_sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainSubjs:
            if trainObj != trainSubj:
                train_sens.append(("The " + trainSubj[0] + ' ' + trainVerb, trainSubj[1], \
                    trainVerb))
                train_sens.append(("The " + trainSubj[0] + ' ' + trainVerb + ' the ' \
                    + trainObj[0], trainSubj[1], trainVerb))
                for subjectRC in subjectRCs:
                    train_sens.append((subjectRC.format(trainSubj[0]) + ' ' + trainVerb, \
                        trainSubj[1], trainVerb))
                    train_sens.append((subjectRC.format(trainSubj[0]) + ' ' + trainVerb +\
                        ' the ' + trainObj[0], trainSubj[1], trainVerb))
                    for objectRC in objectRCs:
                        train_sens.append(("The " + trainSubj[0] + ' ' + trainVerb + ' ' \
                            + objectRC.format(trainObj[0]), trainSubj[1], trainVerb))
                        for itCleft in itClefts:
                            train_sens.append((itCleft.format(trainObj[0]) + " the " + \
                                trainSubj[0] + ' ' + trainVerb, trainSubj[1], trainVerb))
                            for negAdjunct in negAdjuncts:
                                train_sens.append(("The " + trainSubj[0] + ' ' + \
                                    trainVerb + ' ' + negAdjunct.format(trainObj[0]), \
                                    trainSubj[1], trainVerb))
                                for embedClause in embedClauses:
                                    train_sens.append(("The " + trainSubj[0] + ' ' + \
                                        trainVerb + ' the ' + trainObj[0] + ' ' \
                                        + embedClause, trainSubj[1], trainVerb))
                                    for Adjunct in Adjuncts:
                                        train_sens.append(("The " + trainSubj[0] + ' ' + \
                                            trainVerb + ' the ' + trainObj[0] + ' ' \
                                            + Adjunct, trainSubj[1], trainVerb))

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for testObj in testSubjs:
            if testObj != testSubj:
                test_sens.append(("The " + testSubj[0] + ' ' + testVerb, testSubj[1], \
                    testVerb))
                test_sens.append(("The " + testSubj[0] + ' ' + testVerb + ' the ' \
                    + testObj[0], testSubj[1], testVerb))
                for subjectRC in subjectRCs:
                    test_sens.append((subjectRC.format(testSubj[0]) + ' ' + testVerb, \
                        testSubj[1], testVerb))
                    test_sens.append((subjectRC.format(testSubj[0]) + ' ' + testVerb +\
                        ' the ' + testObj[0], testSubj[1], testVerb))
                    for objectRC in objectRCs:
                        test_sens.append(("The " + testSubj[0] + ' ' + testVerb + ' ' \
                            + objectRC.format(testObj[0]), testSubj[1], testVerb))
                        for itCleft in itClefts:
                            test_sens.append((itCleft.format(testObj[0]) + " the " + \
                                testSubj[0] + ' ' + testVerb, testSubj[1], testVerb))
                            for negAdjunct in negAdjuncts:
                                test_sens.append(("The " + testSubj[0] + ' ' + \
                                    testVerb + ' ' + negAdjunct.format(testObj[0]), \
                                    testSubj[1], testVerb))
                                for embedClause in embedClauses:
                                    test_sens.append(("The " + testSubj[0] + ' ' + \
                                        testVerb + ' the ' + testObj[0] + ' ' \
                                        + embedClause, testSubj[1], testVerb))
                                    for Adjunct in Adjuncts:
                                        test_sens.append(("The " + testSubj[0] + ' ' + \
                                            testVerb + ' the ' + testObj[0] + ' ' \
                                            + Adjunct, testSubj[1], testVerb))



random.shuffle(train_sens)
random.shuffle(test_sens)
train_sens = train_sens[:40000]
test_sens = test_sens[:10000]

with open("data/elmo_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in train_sens:
         data_writer.writerow(list(row))

with open("data/elmo_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in test_sens:
         data_writer.writerow(list(row))
