import csv
import random

verbs = open("clean_verbs.txt", 'r').read().split()
present_verbs = open("present_verbs.txt", 'r').read().split()

trainVerbs = verbs[:80]

testVerbs = verbs[80:100]


## Number
trainSubjs = [('person', 0), ('people', 1), ('man', 0), ('men', 1),
    ('woman', 0), ('women', 1), ("linguist", 0), ("linguists", 1), \
    ('priest', 0), ('priests', 1), ('soldiers', 1), ('worker', 0), \
    ('workers', 1), ('actor', 0), ('actors', 1), ('reporter', 0), ('reporters', 1), \
    ('judge', 0), ('judges', 1), ('player', 0)]

# # ('Mouse', 0), , ('Players', 1)
#
testSubjs = [('lackey', 0), ('lackeys', 1), ('boss', 0), \
    ('bosses', 1), ('kid', 0), ('kids', 1), ('friend', 0), \
    ('friends', 1), ('savior', 0), ('saviors', 1), ('doctor', 0), ('doctors', 1)]


## Gender
# trainSubjs = [("man", 0), ("woman", 1), ("men", 0), ("women", 1), ("waiter", 0), \
#         ("waitress", 1), ("actor", 0), ("actress", 1), ("master", 0), ("mistress", 1), \
#         ("son", 0), ("daughter", 1), ("husband", 0), ("wife", 1)]
#
# testSubjs = [("uncle", 0), ("aunt", 1), ("mother", 1), ("father", 0), ("brother", 0), \
#         ("sister", 1), ("girl", 1), ("boy", 0), ("butler", 0), ("maid", 1), ("priest", 0), \
#         ("priestess", 1), ("abbot", 0), ("abbess", 1)]

## Animacy
# trainSubjs = [('dog', 1), ('cat', 1), ('squirrel', 1), ('turtle', 1), ('bird', 1), \
#         ('fish', 1), ('road', 0), ('city', 0), ('fruit', 0), ('vegetable', 0), \
#         ('chair', 0), ('table', 0), ("shirt", 0), ("friend", 1), ("animal", 1), \
#         ("object", 0)]
#
# testSubjs = [('person', 1), ('human', 1), ('man', 1), ('woman', 1), ('horse', 1), \
#         ('bug', 1), ('shoe', 0), ('rock', 0), ('lake', 0), ('sky', 0), ('tree', 0), \
#         ('bush', 0)]

## Tense
# trainSubjs = ['person', 'man', 'woman', 'linguist', 'priest', 'worker', 'actor', \
#         'reporter', 'judge']
# testSubjs = ['player', 'lackey', 'boss', 'kid', 'friend', 'savior', 'doctor']
# trainVerbs = [(verb, 1) for verb in verbs[:40]] + \
#     [(verb, 0) for verb in present_verbs[:40]]
# testVerbs = [(verb, 1) for verb in verbs[80:90]] + \
#     [(verb, 0) for verb in present_verbs[80:90]]

## Distance

# trainAdjs = ["friendly", "helpful", "old", "young", "new"]
# testAdjs = ["good", "bad", "angry", "strange", "normal"]

sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainSubjs:
            # for trainAdj in trainAdjs:
            # if trainSubj[1] != trainObj[1]:
                sens.append(("The " + trainSubj[0] + ' ' + trainVerb + ' the ' + \
                trainObj[0], trainSubj[1]))
                # sens.append(("The " + trainSubj[0] + ' with the ' + trainAdj + ' ' + trainVerb + ' the ' + \
                # trainObj[0], trainSubj[1]))
random.shuffle(sens)
sens = sens[:4000]

with open("../data/subject_number_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))

sens = []

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for testObj in testSubjs:
            # for testAdj in testAdjs:
            # if testSubj[1] != testObj[1]:
                sens.append(("The " + testSubj[0] + ' ' + testVerb + ' the ' \
                + testObj[0], testSubj[1]))
                # sens.append(("The " + testSubj[0] + ' ' + testVerb + ' the ' \
                # + testAdj + ' ' + testObj[0], testSubj[1]))


random.shuffle(sens)
sens = sens[:1000]

with open("../data/subject_number_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
