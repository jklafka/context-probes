from allennlp.commands.elmo import ElmoEmbedder
import csv
# import numpy as np

elmo = ElmoEmbedder()

sentences = []
labels = []
# verb_indices = []
with open("../data/active_train.csv", 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        split_sen = row[0].split()
        sentences.append(split_sen)
        labels.append(row[1])
        # verb_indices.append(split_sen.index(row[2]))

word_embeddings = {0: [],
    1: [],
    2: [],
    3: [],
    4: []}
for sentence in sentences:
    embeddings = elmo.embed_sentence(sentence)
    for i in range(len(sentence)):
        word_embeddings[i].append(embeddings[1, i, :])
    # sen_embedding = np.zeros(1024)
    # embeddings = elmo.embed_sentence(sentences[i])
    # n = embeddings.shape[1]
    # for j in range(n):
    #     sen_embedding += embeddings[1, j, :]
    # sen_embedding /= n
    # sen_embeddings.append(sen_embedding)
    # verb_embeddings.append(embeddings[1, verb_indices[i], :])

for i in range(5):
    with open("../data/elmo_word" + str(i) + "_train.csv", 'w') as dataset:
      csv_writer = csv.writer(dataset, delimiter = ',')
      for j in range(len(word_embeddings[i])):
          csv_writer.writerow(word_embeddings[i][j].tolist() + [labels[j]])


# with open("../data/elmo_sen_train.csv", 'w') as dataset:
#   csv_writer = csv.writer(dataset, delimiter = ',')
#   for i in range(len(sen_embeddings)):
#       csv_writer.writerow(sen_embeddings[i].tolist() + [labels[i]])
#
#
# with open("../data/elmo_verb_train.csv", 'w') as dataset:
#   csv_writer = csv.writer(dataset, delimiter = ',')
#   for i in range(len(verb_embeddings)):
#       csv_writer.writerow(verb_embeddings[i].tolist() + [labels[i]])

sentences = []
labels = []
# verb_indices = []
with open("../data/active_test.csv", 'r') as input_data:
    csv_reader = csv.reader(input_data)
    for row in csv_reader:
        split_sen = row[0].split()
        sentences.append(split_sen)
        labels.append(row[1])

word_embeddings = {0: [],
    1: [],
    2: [],
    3: [],
    4: []}
for sentence in sentences:
    embeddings = elmo.embed_sentence(sentence)
    for i in range(len(sentence)):
        word_embeddings[i].append(embeddings[1, i, :])
    # sen_embedding = np.zeros(1024)
    # embeddings = elmo.embed_sentence(sentences[i])
    # n = embeddings.shape[1]
    # for j in range(n):
    #     sen_embedding += embeddings[1, j, :]
    # sen_embedding /= n
    # sen_embeddings.append(sen_embedding)
    # verb_embeddings.append(embeddings[1, verb_indices[i], :])

for i in range(5):
    with open("../data/elmo_word" + str(i) + "_test.csv", 'w') as dataset:
      csv_writer = csv.writer(dataset, delimiter = ',')
      for j in range(len(word_embeddings[i])):
          csv_writer.writerow(word_embeddings[i][j].tolist() + [labels[j]])

# sentences = []
# labels = []
# # verb_indices = []
# with open("../data/active_test.csv", 'r') as input_data:
#     csv_reader = csv.reader(input_data)
#     for row in csv_reader:
#         split_sen = row[0].split()
#         sentences.append(split_sen)
#         labels.append(row[1])
#         # verb_indices.append(split_sen.index(row[2]))
#
# sen_embeddings = []
# # verb_embeddings = []
# for i in range(len(sentences)):
#     sen_embedding = np.zeros(1024)
#     embeddings = elmo.embed_sentence(sentences[i])
#     n = embeddings.shape[1]
#     for j in range(n):
#         sen_embedding += embeddings[1, j, :]
#     sen_embedding /= n
#     sen_embeddings.append(sen_embedding)
#     # verb_embeddings.append(embeddings[1, verb_indices[i], :])
#
#
# with open("../data/elmo_sen_test.csv", 'w') as dataset:
#   csv_writer = csv.writer(dataset, delimiter = ',')
#   for i in range(len(sen_embeddings)):
#       csv_writer.writerow(sen_embeddings[i].tolist() + [labels[i]])


# with open("../data/elmo_verb_test.csv", 'w') as dataset:
#   csv_writer = csv.writer(dataset, delimiter = ',')
#   for i in range(len(verb_embeddings)):
#       csv_writer.writerow(verb_embeddings[i].tolist() + [labels[i]])
