import csv
# import urllib.request

## FIX THIS
# cola_url = "https://nyu-mll.github.io/CoLA/cola_public_1.1.zip"
# urllib.request.urlretrieve(cola_url)

#maps string of tokens to acceptability rating
sen_d = {}
with open("cola_public/tokenized/in_domain_train.tsv") as tsvfile:
   reader = csv.reader(tsvfile, delimiter='\t')
   for row in reader:
       sen_d[row[3]] = row[1]
