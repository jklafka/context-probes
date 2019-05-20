import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import csv
import argparse

#using the tensorflow universal sentence encoder from Google to construct
#512-dimensional sentence embeddings
embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/2")

parser = argparse.ArgumentParser()
parser.add_argument("data")
parser.add_argument("output")
args = parser.parse_args()
dataname = args.data
output_filename = args.output

sentences = []
messages = []
with open("data/" + dataname, 'r') as simple_data:
    csv_reader = csv.reader(simple_data)
    for row in csv_reader:
        sentences.append((row[0], row[1]))
        messages.append(row[0])

# Reduce logging output.
tf.logging.set_verbosity(tf.logging.ERROR)

with tf.Session() as session:
  session.run([tf.global_variables_initializer(), tf.tables_initializer()])
  message_embeddings = session.run(embed(messages))

  with open("data/" + output_filename, 'w') as dataset:
      csv_writer = csv.writer(dataset, delimiter = ',')
      for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
          csv_writer.writerow(message_embedding + [sentences[i][1]])