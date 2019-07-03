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

trainSubjs = [('Person', 0), ('People', 1), ('Man', 0), ('Men', 1),
    ('Woman', 0), ('Women', 1), ("Linguist", 0), ("Linguists", 1), \
    ('Goose', 0), ('Geese', 1), ('Mice', 1), ('Ox', 0), \
    ('Oxen', 1), ('Actor', 0), ('Actors', 1), ('Narwhal', 0), ('Narwhals', 1), \
    ('Judge', 0), ('Judges', 1), ('Player', 0)]

# ('Mouse', 0), , ('Players', 1)

testSubjs = [('Dog', 0), ('Dogs', 1), ('Cat', 0), \
    ('Cats', 1), ('Bird', 0), ('Birds', 1), ('Friend', 0), ('Friends', 1), \
    ('Savior', 0), ('Saviors', 1), ('Doctor', 0), ('Doctors', 1)]

# trainObj[0]s = ['cheese', 'cheeses', 'jar', 'jars', 'vase', 'vases', 'bike', \
#     'bikes', 'bear', 'bears', 'armadillo', 'armadillos', 'lawyer', 'lawyers', '\
#     business', 'businesses', 'buddy', 'buddies', 'flower', 'flowers']
#
# testObjs = ['store', 'stores', 'student', 'students', 'painter', 'painters', \
#     'teacher', 'teachers']

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


for trainVerb in trainVerbs:
    for trainSubj in trainSubjs:
        for trainObj in trainSubjs:
            if trainObj[1] != trainSubj[1]:
                sens.append(("The " + trainSubj[0] + ' ' + trainVerb, trainSubj[1]))
                sens.append(("The " + trainSubj[0] + ' ' + trainVerb + ' ' \
                    + trainObj[0], trainSubj[1]))
                for subjectRC in subjectRCs:
                    sens.append((subjectRC.format(trainSubj[0]) + ' ' + trainVerb, \
                        trainSubj[1]))
                    sens.append((subjectRC.format(trainSubj[0]) + ' ' + trainVerb +\
                        ' ' + trainObj[0], trainSubj[1]))
                    for objectRC in objectRCs:
                        sens.append(("The " + trainSubj[0] + ' ' + trainVerb + ' ' \
                            + objectRC.format(trainObj[0]), trainSubj[1]))
                        for itCleft in itClefts:
                            sens.append((itCleft.format(trainObj[0]) + " the " + \
                                trainSubj[0] + ' ' + trainVerb, trainSubj[1]))
                            for negAdjunct in negAdjuncts:
                                sens.append(("The " + trainSubj[0] + ' ' + \
                                    trainVerb + ' ' + negAdjunct.format(trainObj[0]), \
                                    trainSubj[1]))
                                for embedClause in embedClauses:
                                    sens.append(("The " + trainSubj[0] + ' ' + \
                                        trainVerb + ' ' + trainObj[0] + ' ' \
                                        + embedClause, trainSubj[1]))
                                    for Adjunct in Adjuncts:
                                        sens.append(("The " + trainSubj[0] + ' ' + \
                                            trainVerb + ' ' + trainObj[0] + ' ' \
                                            + Adjunct, trainSubj[1]))

random.shuffle(sens)

sens = sens[:40000]

with open("data/new_train.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))

# all_clauses = subjectRCs + objectRCs + itClefts + negAdjuncts + embedClauses \
#     + Adjuncts
#
# all_words = Pronouns + trainObj[0]s + testObjs + trainVerbs + testVerbs
#
# all_subjs
#
#
#
# vocab_list = []
# for part in all_parts:
#     words = part[0].split()
#     for word in words:
#         if word.lower() not in vocab_list:
#             vocab_list.append(word.lower())
# print(vocab_list)
# import json
#
# with open("glove/glove_dict.json", 'r') as json_file:
#     vocab_dict = json.load(json_file)
# task_dict = {key:val for key, val in vocab_dict.items() if key in vocab_list}
# for key, val in task_dict.items():
#     print(key)
# with open("task_vocab.json", 'w') as task_json:
#     json.dump(task_dict, task_json)
