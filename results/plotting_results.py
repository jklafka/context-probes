import matplotlib, argparse
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("experiment")
parser.add_argument("task")
args = parser.parse_args()

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

base = pd.read_csv("acl/base_tasks.csv")
distance = pd.read_csv("acl/distance_tasks.csv")
identity = pd.read_csv("acl/word_identity.csv")

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()
