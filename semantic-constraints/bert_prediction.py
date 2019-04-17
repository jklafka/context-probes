## modify the text and masked_index

import torch
import numpy as np
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenized input
text = "[CLS] My family went to the beach . [SEP] I drank water . [SEP]"
tokenized_text = tokenizer.tokenize(text)

# Mask a token that we will try to predict back with `BertForMaskedLM`
masked_index = 11
original = tokenized_text[masked_index]
tokenized_text[masked_index] = '[MASK]'

# Convert token to vocabulary indices
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
# Define sentence A and B indices associated to 1st and 2nd sentences (see paper)
len_first = tokenized_text.index("[SEP]")
segments_ids = [0] * len_first + [1] * (len(tokenized_text) - len_first)

# Convert inputs to PyTorch tensors
tokens_tensor = torch.tensor([indexed_tokens])
segments_tensors = torch.tensor([segments_ids])

# Load pre-trained model (weights)
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
model.eval()

# Predict all tokens
with torch.no_grad():
    predictions = model(tokens_tensor, segments_tensors)

predicted_indices = torch.topk(predictions[0, masked_index], k = 10)[1]
predicted_indices = list(np.array(predicted_indices))
predicted_tokens = tokenizer.convert_ids_to_tokens(predicted_indices)
print(text)
print(original)
print(predicted_tokens)
