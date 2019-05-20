import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/elmo_sen_train.csv", header=None)
X_train = df.loc[:, :1023] #first 512 columns are embeddings
Y_train = df.loc[:, 1024] #last column is class label

df = pd.read_csv("data/elmo_sen_test.csv", header=None)
X_test = df.loc[:, :1023] #first 512 columns are embeddings
Y_test = df.loc[:, 1024] #last column is class label
print(sum(Y_train)/Y_train.shape[0])
print(sum(Y_test)/Y_test.shape[0])

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20)

## Use Multi-Layer Perceptron
mlp = MLPClassifier(hidden_layer_sizes = (20, 20, 20), \
    max_iter = 1000, \
    alpha = .001, solver = "sgd")

mlp.fit(X_train, Y_train)
print(mlp.score(X_test, Y_test))