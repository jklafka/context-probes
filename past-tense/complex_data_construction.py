import csv
import random

verbs = []

with open("data/all_verbs.csv", 'r') as f:
     csv_reader = csv.reader(f)
     for row in csv_reader:
         verbs.append(row[0])
verbs = verbs[1:]

subjects = [('I', 0), ('We', 1), ('It', 0), ('They', 1), ('Person', 0), \
    ('People', 1), ('Man', 0), ('Men', 1), ('Woman', 0), ('Women', 1), \
    ('Goose', 0), ('Geese', 1), ('Mouse', 0), ('Mice', 1), ('Ox', 0), \
    ('Oxen', 1)]

adjuncts = ["in my house", "with my father", "with my fathers", "in our house"]

sens = []

for item in subjects:
     for verb in verbs:
         j = random.randint(0, len(adjuncts) - 1)
         sens.append((item[0] + ' ' + verb + ' ' + adjuncts[j], item[1]))

random.shuffle(sens)

with open("data/complex_data.csv", 'w') as csv_file:
     data_writer = csv.writer(csv_file, delimiter = ',')
     for row in sens:
         data_writer.writerow(list(row))
