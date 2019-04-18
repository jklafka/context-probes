import csv
import random

verbs = []

with open("data/all_verbs.csv", 'r') as f:
     csv_reader = csv.reader(f)
     for row in csv_reader:
         verbs.append(row[0])
verbs = verbs[1:]

trainVerbs = verbs[:401]

testVerbs = verbs[401:]

Pronouns = [('I', 0), ('We', 1), ('It', 0), ('They', 1)]

trainNouns = [('Person', 0), ('People', 1), ('Man', 0), ('Men', 1),
    ('Woman', 0), ('Women', 1), ("Linguist", 0), ("Linguists", 1) \
    ('Goose', 0), ('Geese', 1), ('Mouse', 0), ('Mice', 1), ('Ox', 0), \
    ('Oxen', 1), ('Sloth', 0), ('Sloths', 1), ('Narwhal', 0), ('Narwhals', 1), \
    ('Judge', 0), ('Judges', 1), ('Engineer', 0), ('Engineers', 1)]

testNouns = [('Dog', 0), ('Dogs', 1), ('Cat', 0), \
    ('Cats', 1), ('Bird', 0), ('Birds', 1), ('Friend', 0), ('Friends', 1), \
    ('Savior', 0), ('Saviors', 1), ('Doctor', 0), ('Doctors', 1)]

subjectRCs = [""]

objectRCs = [""]

itClefts = ["It was the {} that"]

negAdjuncts = ["but not the {}", "without the {}"]

embedClauses = ["that we found", "that I found", "that she created", \
    "that they created"]

Adjuncts = ["in my house", "with my father", "with my fathers", "in our house"]

sens = []

# for item in subjects:
#      for verb in verbs:
#          j = random.randint(0, len(adjuncts) - 1)
#          sens.append((item[0] + ' ' + verb + ' ' + adjuncts[j], item[1]))

random.shuffle(sens)

with open("data/complex_data.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
