import torch
import torch.nn as nn
import random
import time
import math
import json

with open("corpus.json", 'r') as f:
    sen_d = json.load(f)
vocab = set()
for key, val in sen_d.items():
    vocab = vocab | set(key.split())
vocab = list(vocab)
vocab_size = len(vocab) #number of distinct tokens from CoLA

sen_list = [(key, val) for key, val in sen_d.items()]

acceptable = ["No", "Yes"]

def sentenceToTensor(sentence):
    tensor = torch.zeros(len(sentence), 1, vocab_size)
    tokens = sentence.split()
    token_list = zip(range(len(tokens)), tokens)
    for ti, token in token_list:
        tensor[ti][0][vocab.index(token)] = 1
    return tensor

def acceptabilityTensor(rating):
    return torch.tensor([rating], dtype=torch.long)

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
criterion = nn.NLLLoss()

learning_rate = 0.005

def get_training_item():
    sentence, rating = sen_list[random.randint(0, len(sen_list)-1)]
    sen_tensor = sentenceToTensor(sentence)
    rating_tensor = acceptabilityTensor(int(rating))
    return sentence, rating, sen_tensor, rating_tensor


def train(sentence_tensor, acceptability_tensor):
    hidden = rnn.initHidden()
    rnn.zero_grad()

    for i in range(sentence_tensor.size()[0]):
        output, hidden = rnn(sentence_tensor[i], hidden)
    print(output, acceptability_tensor)
    loss = criterion(output, acceptability_tensor)
    loss.backward()
    for p in rnn.parameters():
        p.data.add_(-learning_rate, p.grad.data)

    return output, loss.item()



n_iters = 1000
print_every = 50
# plot_every = 1000

current_loss = 0
all_losses = []

def timeSince(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

start = time.time()

for iter in range(1, n_iters + 1):
    sentence, rating, sentence_tensor, rating_tensor = get_training_item()
    output, loss = train(sentence_tensor, rating_tensor)
    current_loss += loss

    if iter % print_every == 0:
        guess, guess_i = acceptability(output)
        correct = '✓' if guess == rating else '✗ (%s)' % rating
        print('%d %d%% (%s) %.4f %s / %s %s' % (iter, iter / n_iters * 100, \
            timeSince(start), loss, sentence, guess, correct))
    #
    # if iter % plot_every == 0:
    #     all_losses.append(current_loss / plot_every)
    #     current_loss = 0

# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
#
# plt.figure()
# plt.plot(all_losses)
