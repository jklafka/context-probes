import nltk
#nltk.download('averaged-perceptron-tagger')

f = open("vocab.txt", 'r') # bert base uncased vocab txt file
vocab = f.readlines()
vocab = vocab[2000:] # take out the unknown tokens and Chinese characters
vocab = [word.strip('\n') for word in vocab]

# now use POS taggers
vocab = [word for word in vocab if nltk.pos_tag(word)[0][1] == "NN"]
