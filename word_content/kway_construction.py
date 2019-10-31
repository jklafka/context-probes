import csv, random

target_name = "verb"
assert target_name in ["subject", "object", "verb"], \
    "enter a valid content word type"

num_mappings = 30
# to leave enough nouns for the other noun (subj or obj)
assert num_mappings < 50, "enter a number of mappings under 50"

# read in verbs and vocabulary indices
verbs = []
verb_list = open("../stimuli/clean_verbs.txt", 'r').read().split()
random.shuffle(verb_list)
for i, verb in enumerate(verb_list):
    verbs.append([verb, i])

# read in nouns and vocabulary indices
nouns, noun_list = [], []
with open("../stimuli/other_nouns.csv", 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        noun_list.append(line[0]) #vocabulary index for one-hot vectors
random.shuffle(noun_list)
for i, noun in enumerate(noun_list):
    nouns.append([noun, i])


# set the train and test to be the same for the target
# create train-test split for the other categories
if target_name == "verb":
    trainVerbs = verbs[:num_mappings]
    testVerbs = trainVerbs
    trainSubjs = nouns[:25]
    testSubjs = nouns[25:50]
    trainObjs = nouns[50:75]
    testObjs = nouns[75:100]

elif target_name == "subject":
    trainSubjs = nouns[:num_mappings]
    testSubjs = trainSubjs
    trainObjs = nouns[50:75]
    testObjs = nouns[75:100]
    trainVerbs = verbs[:50]
    testVerbs = verbs[50:]

elif target_name == "object":
    trainObjs = nouns[:num_mappings]
    testObjs = trainObjs
    trainSubjs = nouns[50:75]
    testSubjs = nouns[75:100]
    trainVerbs = verbs[:50]
    testVerbs = verbs[50:]


# create train set: every sentence is paired with the target word's vocab index
sens = []
for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
         for trainObj in trainObjs:
            # which word should we get the vocab index from?
            if target_name == "verb":
                target = trainVerb
            elif target_name == "subject":
                target = trainSubj
            elif target_name == "object":
                target = trainObj
            # each stim has the form (sentence, vocab index)
            sens.append(("the " + trainSubj[0] + ' ' + trainVerb[0] + " the " + \
                trainObj[0], target[1]))

random.shuffle(sens)
sens = sens[:4000]

with open("../data/kway/" + target_name + "/train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))


# create test set
sens = []
for testVerb in testVerbs:
    for testSubj in testSubjs:
         for testObj in testObjs:
            if target_name == "verb":
                target = testVerb
            elif target_name == "subject":
                target = testSubj
            elif target_name == "object":
                target = testObj
            # each stim has the form (sentence, vocab index)
            sens.append(("the " + testSubj[0] + ' ' + testVerb[0] + " the " + \
                testObj[0], target[1]))

random.shuffle(sens)
sens = sens[:1000]

with open("../data/kway/" + target_name + "/test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
