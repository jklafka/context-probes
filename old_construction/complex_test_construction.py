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

Pronouns = [('I', 0), ('We', 1), ('It', 0), ('They', 1)]

testSubjs = [('Dog', 0), ('Dogs', 1), ('Cat', 0), \
    ('Cats', 1), ('Bird', 0), ('Birds', 1), ('Friend', 0), ('Friends', 1), \
    ('Savior', 0), ('Saviors', 1), ('Doctor', 0), ('Doctors', 1)]

subjectRCs = ["The {} that I wanted", "The {} that we wanted", \
    "The {} that they liked", "The {} that he wanted"]

objectRCs = ["that she created", "that they created", \
    "that I found", "that we found"]

itClefts = ["It was the {} that"]

negAdjuncts = ["but not the {}", "without the {}"]

embedClauses = ["that we found", "that I found", "that she created", \
    "that they created"]

Adjuncts = ["in my house", "with my father", "with my fathers", "in our house"]

sens = []

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for testObj in testSubjs:
            if testObj[1] != testSubj[1]:
                sens.append(("The " + testSubj[0] + ' ' + testVerb, testSubj[1]))
                sens.append(("The " + testSubj[0] + ' ' + testVerb + ' ' \
                    + testObj[0], testSubj[1]))
                for subjectRC in subjectRCs:
                    sens.append((subjectRC.format(testSubj[0]) + ' ' + testVerb, \
                        testSubj[1]))
                    sens.append((subjectRC.format(testSubj[0]) + ' ' + testVerb +\
                        ' ' + testObj[0], testSubj[1]))
                    for objectRC in objectRCs:
                        sens.append(("The " + testSubj[0] + ' ' + testVerb + ' ' \
                            + objectRC.format(testObj[0]), testSubj[1]))
                        for itCleft in itClefts:
                            sens.append((itCleft.format(testObj[0]) + " the " + \
                                testSubj[0] + ' ' + testVerb, testSubj[1]))
                            for negAdjunct in negAdjuncts:
                                sens.append(("The " + testSubj[0] + ' ' + \
                                    testVerb + ' ' + negAdjunct.format(testObj[0]), \
                                    testSubj[1]))
                                for embedClause in embedClauses:
                                    sens.append(("The " + testSubj[0] + ' ' + \
                                        testVerb + ' ' + testObj[0] + ' ' \
                                        + embedClause, testSubj[1]))
                                    for Adjunct in Adjuncts:
                                        sens.append(("The " + testSubj[0] + ' ' + \
                                            testVerb + ' ' + testObj[0] + ' ' \
                                            + Adjunct, testSubj[1]))

random.shuffle(sens)

sens = sens[:10000]

with open("data/new_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
