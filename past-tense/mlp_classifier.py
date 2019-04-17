import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("data/dataset.csv", header=None)
X = df.loc[:, :511] #first 512 columns are embeddings
Y = df.loc[:, 512] #last column is class label

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20)

mlp = MLPClassifier(hidden_layer_sizes = (20, 20, 20), \
    max_iter = 1000, \
    alpha = .001, solver = "sgd")

mlp.fit(X_train, Y_train)
print(mlp.score(X_test, Y_test))

# Y_hat = mlp.predict(X_test)
#
# cm = confusion_matrix(Y_test, Y_hat)
# print(cm)
# sns.heatmap(cm, center=True)
# plt.show()
