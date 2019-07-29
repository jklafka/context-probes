import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# print("The train balance is {}".format(sum(Y_train)/Y_train.shape[0]))
# print("The test balance is {}".format(sum(Y_test)/Y_test.shape[0]))

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20)

## Use Logistic Regression
for i in range(5):
    df = pd.read_csv("../data/glove_word" + str(i) + "_train.csv", header=None)
    X_train = df.iloc[:, :-1] #first n-1 columns are embeddings
    Y_train = df.iloc[:, -1] #last column is class label

    df = pd.read_csv("../data/glove_word" + str(i) + "_test.csv", header=None)
    X_test = df.iloc[:, :-1] #first n-1 columns are embeddings
    Y_test = df.iloc[:, -1] #last column is class label
    lr = LogisticRegression()
    lr.fit(X_train, Y_train)

    Y_hat = lr.predict(X_test)
# X = pd.read_csv("../data/elmo_test.csv", header=None)
# X[2] = Y_hat
# X.to_csv("pred.csv")
    print("Using word " + str(i))
    print(lr.score(X_test, Y_test))
