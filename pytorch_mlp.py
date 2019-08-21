import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import csv
import numpy as np

trainset = []
trainlabels = []
with open("train.csv", 'r') as train:
    reader = csv.reader(train)
    for row in reader:
        trainset.append(list(map(float, row[:-1])))
        label = int(row[-1])
        temp = [0, 0]
        temp[label] = 1
        trainlabels.append(temp)
trainset = torch.FloatTensor(trainset)
trainlabels = torch.FloatTensor(trainlabels)

testset = []
testlabels = []
with open("test.csv", 'r') as test:
    reader = csv.reader(test)
    for row in reader:
        testset.append(list(map(float, row[:-1])))
        label = int(row[-1])
        temp = [0, 0]
        temp[label] = 1
        testlabels.append(temp)
testset = torch.FloatTensor(testset)
testlabels = torch.FloatTensor(testlabels)


class simple_3layer(nn.Module):
    def __init__(self, input_dim, hidden_dims):
        super().__init__()
        self.lin1 = nn.Linear(input_dim, hidden_dims[0], bias = True)
        self.lin2 = nn.Linear(hidden_dims[0], hidden_dims[1], bias = True)
        self.lin3 = nn.Linear(hidden_dims[1], hidden_dims[2], bias = True)
        self.linout = nn.Linear(hidden_dims[2], 2)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, x):
        output = F.relu(self.lin1(x))
        output = F.relu(self.lin2(output))
        output = F.relu(self.lin3(output))
        output = F.relu(self.linout(output))
        output = self.softmax(output)
        return output

model = simple_3layer(300, (20, 20, 20))
criterion = nn.MSELoss(reduction='sum')
optimizer = optim.SGD(model.parameters(), lr=1e-4, momentum=0.9)

for epoch in range(2):  # loop over the dataset multiple times
    # zero the parameter gradients
    optimizer.zero_grad()

    # forward + backward + optimize
    # for i in range(len(trainset)):
    output = model(trainset)
    loss = criterion(output, trainlabels)
    loss.backward()
    optimizer.step()

print('Finished Training')

correct = 0
total = 0
with torch.no_grad():
    output = model(testset[i])
    predicted = float(torch.max(output, 1)[1])
    total += 1
    correct += (predicted == testlabels[i].item())
print(correct/total)
