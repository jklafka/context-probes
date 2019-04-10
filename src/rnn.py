import torch
import torch.nn as nn

vocab = set()
for key, val in sen_d.items():
    vocab = vocab | set(key.split())
vocab = list(vocab)
vocab_size = len(vocab) #number of distinct tokens from CoLA

acceptable = ["No", "Yes"]

def sentenceToTensor(sentence):
    tensor = torch.zeros(len(sentence), 1, vocab_size)
    for wi, word in enumerate(sentence):
        tensor[wi][0][vocab.find(word)] = 1
    return tensor


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.inner_hidden = nn.Linear(input_size + hidden_size, hidden_size)
        self.inner = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.inner_hidden(combined)
        output = self.inner(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)


def acceptability(output):
    top_n, top_i = output.topk(1)
    rating = top_i[0].item()
    return acceptable[rating], rating


n_hidden = 128
rnn = RNN(vocab_size, n_hidden, 2) # 2 categories: acceptable and unacceptable
