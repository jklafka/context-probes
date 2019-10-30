import torch, csv, logging, argparse
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

## set up logging
parser = argparse.ArgumentParser()
parser.add_argument("logname")
args = parser.parse_args()
logging.basicConfig(filename = "results/" + args.logname + ".csv", format="%(message)s", level=logging.INFO)

# get CUDA device
device = torch.device("cuda:0")

## define neural networks: first has three hidden layers
class ThreeLayerNet(nn.Module):
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

## this neural net has only one hidden layer
class OneLayerNet(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.lin1 = nn.Linear(input_dim, 1024, bias = True)
        self.linout = nn.Linear(1024, 2)

    def forward(self, x):
        output = F.relu(self.lin1(x))
        output = F.relu(self.linout(output))
        return output

# record the different reps we're using
REPS = ["bert", "elmo", "gpt", "glove"]

for _ in range(10):
    for rep in REPS:
        # for each word
        for i in range(5):
            trainset = []
            trainlabels = []
            with open("data/" + rep + "/train" + str(i) + ".csv", 'r') as train:
                reader = csv.reader(train)
                for row in reader:
                    trainset.append(list(map(float, row[:-1])))
                    trainlabels.append(row[-1])
            trainset = torch.FloatTensor(trainset).to(device)
            trainlabels = [int(label) for label in trainlabels]
            trainlabels = torch.LongTensor(trainlabels).to(device)

            testset = []
            testlabels = []
            with open("data/" + rep + "/test" + str(i) + ".csv", 'r') as test:
                reader = csv.reader(test)
                for row in reader:
                    testset.append(list(map(float, row[:-1])))
                    testlabels.append(row[-1])
            testset = torch.FloatTensor(testset).to(device)
            testlabels = [int(label) for label in testlabels]
            testlabels = torch.LongTensor(testlabels).to(device)

            # define the architectures we're working with
            smallnet = ThreeLayerNet(trainset[0].shape[0], (20,20,20))
            smallnet.to(device)
            bignet = ThreeLayerNet(trainset[0].shape[0], (1024,1024,1024))
            bignet.to(device)
            singlelayer = OneLayerNet(trainset[0].shape[0])
            singlelayer.to(device)
            netdict = {smallnet: "20_20_20", bignet: "1024_1024_1024", \
                singlelayer: "1024"}

            for net in netdict:
                criterion = nn.CrossEntropyLoss()
                optimizer = optim.Adam(net.parameters(), lr=0.001)

                for epoch in range(1000):  # loop over the dataset multiple times

                    # zero the parameter gradients
                    optimizer.zero_grad()

                    # forward + backward + optimize
                    outputs = net(trainset)
                    loss = criterion(outputs, trainlabels)
                    loss.backward()
                    optimizer.step()

                    # print statistics

                correct = 0
                total = 0
                with torch.no_grad():
                    outputs = net(testset)
                    _, predicted = torch.max(outputs.data, 1)
                    total += testlabels.size(0)
                    correct += (predicted == testlabels).sum().item()

                    logging.info(rep + ',' + netdict[net] + ',' + str(i) + ',' + \
                        str(100 * correct/total))
