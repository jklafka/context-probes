from allennlp.modules.elmo import Elmo, batch_to_ids

options_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_options.json"
weight_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"

# Compute two different representation for each token.
# Each representation is a linear weighted combination for the
# 3 layers in ELMo (i.e., charcnn, the outputs of the two BiLSTM))
elmo = Elmo(options_file, weight_file, 2, dropout=0)

# use batch_to_ids to convert sentences to character ids
sentence = [['The', 'doctor', 'punched', 'the', 'scientist', '.']]
character_ids = batch_to_ids(sentence)

embeddings = elmo(character_ids)
# print(embeddings)

'''
Procedure: for each sentence, split it into words/punctuation.
batch_to_ids to convert the sentence into a format elmo can work with.
Then create the embeddings. You get a dictionary mapping 'elmo_representations'
    to a list of torch tensors, each of which is dim number of sentences x number
    of layers x number of dimensions of each representation
Create 6 output files: {combining the two reps; first rep; second rep} X
    {only the verb we care about; the entire sentence}
'''
