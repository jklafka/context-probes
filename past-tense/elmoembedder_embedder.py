from allennlp.commands.elmo import ElmoEmbedder
elmo = ElmoEmbedder()
tokens = ["I", "ate", "an", "apple", "for", "breakfast"]
vectors = elmo.embed_sentence(tokens)

import scipy
vectors2 = elmo.embed_sentence(["I", "ate", "a", "carrot", "for", "breakfast"])
scipy.spatial.distance.cosine(vectors[2][3], vectors2[2][3])
# cosine distance between "apple" and "carrot" in the last layer
