import torch
import csv
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


trainset = []
trainlabels = []
with open("data/train.csv", 'r') as train:
    reader = csv.reader(train)
    for row in reader:
        trainset.append(list(map(float, row[:-1])))
        # label = int(row[-1])
        # temp = [0, 0]
        # temp[label] = 1
        trainlabels.append(row[-1])
trainset = torch.FloatTensor(trainset)
trainlabels = [int(label) for label in trainlabels]
trainlabels = torch.LongTensor(trainlabels)

testset = []
testlabels = []
with open("data/test.csv", 'r') as test:
    reader = csv.reader(test)
    for row in reader:
        testset.append(list(map(float, row[:-1])))
        testlabels.append(row[-1])
testset = torch.FloatTensor(testset)
testlabels = [int(label) for label in testlabels]
testlabels = torch.LongTensor(testlabels)


class Net(nn.Module):
    def __init__(self, input_dim, hidden_dims):
        super().__init__()
        self.lin1 = nn.Linear(input_dim, hidden_dims[0], bias = True)
        self.lin2 = nn.Linear(hidden_dims[0], hidden_dims[1], bias = True)
        self.lin3 = nn.Linear(hidden_dims[1], hidden_dims[2], bias = True)
        self.linout = nn.Linear(hidden_dims[2], 2)

    def forward(self, x):
        output = F.relu(self.lin1(x))
        output = F.relu(self.lin2(output))
        output = F.relu(self.lin3(output))
        output = F.relu(self.linout(output))
        return output


net = Net(300, (20,20,20))


criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(1000):  # loop over the dataset multiple times
    running_loss = 0.0

    # zero the parameter gradients
    optimizer.zero_grad()

    # forward + backward + optimize
    outputs = net(trainset)
    loss = criterion(outputs, trainlabels)
    loss.backward()
    optimizer.step()

    # print statistics
    running_loss += loss.item()
    print(running_loss)

print('Finished Training')


correct = 0
total = 0
with torch.no_grad():
    outputs = net(testset)
    _, predicted = torch.max(outputs.data, 1)
    total += testlabels.size(0)
    correct += (predicted == testlabels).sum().item()

print('Accuracy of the network on the 1000 test: %d %%' % (
    100 * correct / total))
