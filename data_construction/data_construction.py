import csv
import random

verbs = open("clean_verbs.txt", 'r').read().split()
# present_verbs = open("present_verbs.txt", 'r').read().split()

trainVerbs = verbs[:80]

testVerbs = verbs[80:100]


# ## Number
# trainSubjs = [('person', 0), ('people', 1), ('man', 0), ('men', 1),
#     ('woman', 0), ('women', 1), ("linguist", 0), ("linguists", 1), \
#     ('priest', 0), ('priests', 1), ('soldiers', 1), ('worker', 0), \
#     ('workers', 1), ('actor', 0), ('actors', 1), ('reporter', 0), ('reporters', 1), \
#     ('judge', 0), ('judges', 1), ('player', 0)]
#
# # # ('Mouse', 0), , ('Players', 1)
# #
# testSubjs = [('lackey', 0), ('lackeys', 1), ('boss', 0), \
#     ('bosses', 1), ('kid', 0), ('kids', 1), ('friend', 0), \
#     ('friends', 1), ('savior', 0), ('saviors', 1), ('doctor', 0), ('doctors', 1)]


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

## Verbs
trainSubjs = ['person', 'man', 'woman', 'linguist', 'priest', 'worker', 'actor', \
        'reporter', 'judge', 'farmer', 'traveler', 'painter', 'actress', 'genius', \
        'fool', 'performer', 'student', 'teacher', 'athlete', 'activist', 'donor', \
        'professor', 'philosopher']
testSubjs = ['player', 'lackey', 'boss', 'kid', 'friend', 'savior', 'doctor', \
        'pedestrian', 'jester', 'politician', 'runner', 'nurse', 'leader', 'mechanic',\
        'priest', 'biker']
## Tense
# trainVerbs = [(verb, 1) for verb in verbs[:40]] + \
#     [(verb, 0) for verb in present_verbs[:40]]
# testVerbs = [(verb, 1) for verb in verbs[80:90]] + \
#     [(verb, 0) for verb in present_verbs[80:90]]

## Dynamic vs stative
# dynamic = ["helped", "improved", "interviewed", "introduced", "justified", \
#     "persuaded", "saved", "showed", "studied", "targeted", "transformed", \
#     "treated", "uncovered", "unveiled", "validated", "valued", "wrote", "ate", \
#     "hit", "buried"]
# labels = [1] * len(dynamic)
# dynamic = list(zip(dynamic, labels))
# static = ["believed", "concerned", "disliked", "doubted", "hated", "heard", "impressed", \
#     "knew", "liked", "loved", "needed", "owned", "preferred", "promised", "recognized", \
#     "remember", "surprised", "understood", "smelled", "perceived"]
# labels = [0] * len(static)
# static = list(zip(static, labels))
# trainVerbs = dynamic[:15] + static[:15]
# testVerbs = dynamic[15:] + static[15:]

## Distance

# trainAdjs = ["friendly", "helpful", "old", "young", "new"]
# testAdjs = ["good", "bad", "angry", "strange", "normal"]

## Quantifiers
quantifiers = [('all', 1), ('every', 1), ('some', 0), ('a', 0)]

sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainSubjs:
            for quantifier in quantifiers:
            # for trainAdj in trainAdjs:
            # if trainSubj[1] != trainObj[1]:
                sens.append((quantifier[0] + ' ' + trainSubj + ' ' + trainVerb + " the " + \
                trainObj, quantifier[1]))
                # sens.append(("The " + trainSubj[0] + ' with the ' + trainAdj + ' ' + trainVerb + ' the ' + \
                # trainObj[0], trainSubj[1]))
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
            for quantifier in quantifiers:
            # for testAdj in testAdjs:
            # if testSubj[1] != testObj[1]:
                sens.append((quantifier[0] + ' ' + testSubj + ' ' + testVerb + " the " + \
                testObj, quantifier[1]))
                # sens.append(("The " + testSubj[0] + ' ' + testVerb + ' the ' \
                # + testAdj + ' ' + testObj[0], testSubj[1]))


random.shuffle(sens)
sens = sens[:1000]

with open("../data/quant_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
