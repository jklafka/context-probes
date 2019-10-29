import csv, random, argparse

parser = argparse.ArgumentParser()
parser.add_argument("target_name", help="which type of word to target")
parser.add_argument("output_name", help="which type of linguistic information to probe for")
args = parser.parse_args()

target_name = args.target_name
output_name = args.output_name

assert target_name in ["subject", "object", "verb"], \
    "enter a valid content word type"

num_train = 80
num_test = 100

## subject and object probing tasks
if target_name == "subject" or target_name == "object":
    assert output_name in ["number", "gender", "animacy"], \
        "enter a valid linguistic property to probe for"
    nouns = []
    ## number
    if output_name == "number":
        with open("../stimuli/number_nouns.csv", 'r') as f:
             reader = csv.reader(f)
             for line in reader:
                 nouns.append((line[0], 0))
                 nouns.append((line[1], 1))

    ## gender
    elif output_name == "gender":
        with open("../stimuli/gender_nouns.csv", 'r') as f:
             reader = csv.reader(f)
             for line in reader:
                 nouns.append((line[0], int(line[1])))
                 num_train = 30
                 num_test = 40

    ## animacy
    elif output_name == "animacy":
        with open("../stimuli/animacy_nouns.csv", 'r') as f:
             reader = csv.reader(f)
             for line in reader:
                 nouns.append((line[0], 0))
                 nouns.append((line[1], 1))

    # set up verbs
    verbs = open("../stimuli/clean_verbs.txt", 'r').read().split()
    trainVerbs = list(zip(verbs[:80], ['a']*80))
    testVerbs = list(zip(verbs[80:100], ['a']*80))

elif target_name == "verb":
    assert output_name in ["tense", "dynamic", "stative", "argument", "alternating"], \
        "enter a valid linguistic property to probe for"
    verbs = []

    if output_name == "tense":
        present_verbs = open("../stimuli/present_verbs.txt", 'r').read().split()
        trainVerbs = list(zip(verbs[:40], [1] * 40)) + \
            list(zip(present_verbs[:40], [0] * 40))
        testVerbs = list(zip(verbs[81:90], [1] * 10)) + \
            list(zip(present_verbs[81:90], [0] * 10))
        # get subjects and objects

    elif output_name == "dynamic" or output_name == "stative":
        # read in training and testing verbs
        with open("../stimuli/dynamic_verbs.csv", 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                verbs.append(line)
        trainVerbs = verbs[:30]
        testVerbs = verbs[30:]
        # get subjects and objects

    elif output_name == "argument":
        # read in training and testing verbs
        with open("../stimuli/argument_verbs.csv", 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                verbs.append(line)
        trainVerbs = verbs[:80]
        testVerbs = verbs[80:]

    elif output_name == "alternating":
        # read in training and testing verbs
        # causative verbs are marked with a 0
        # inchoative verbs are marked with a 1
        with open("../stimuli/alternating_verbs.csv", 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                verbs.append(line)
        trainVerbs = verbs[:80]
        testVerbs = verbs[80:]

    # get subjects and objects
    nouns = []
    with open("../stimuli/other_nouns.csv", 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            nouns.append((line[0],'a'))


# create trainset
trainSubjs = nouns[:num_train+1]
testSubjs = nouns[num_train+1:num_test]

sens = []

for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainSubjs:
            if trainObj != trainSubj:
                if target_name == "verb":
                    target = trainVerb
                elif target_name == "subject":
                    target = trainSubj
                elif target_name == "object":
                    target = trainObj
                sens.append(("the " + trainSubj[0] + ' ' + trainVerb[0] + " the " + \
                    trainObj[0], target[1]))

random.shuffle(sens)
sens = sens[:4000]

# write to data folder in *local* repo
with open("../data/" + target_name + '_' + output_name + "_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))

# now create testing set--analogous to training set construction
sens = []

for testVerb in testVerbs:
    for testSubj in testSubjs:
        for testObj in testSubjs:
            if testObj != testSubj:
                if target_name == "verb":
                    target = testVerb
                elif target_name == "subject":
                    target = testSubj
                elif target_name == "object":
                    target = testObj
                sens.append(("the " + testSubj[0] + ' ' + testVerb[0] + " the " + \
                    testObj[0], target[1]))


random.shuffle(sens)
sens = sens[:1000]

with open("../data/" + target_name + '_' + output_name + "_test.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
