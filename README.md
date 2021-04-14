# context-probes
What is the "context" in a contextual word vector? We investigate what vectors from popular encoders such as BERT and ELMo, along with a non-contextual GLoVe baseline, encode about their contexts.

## process

In order to run the full_probes.sh script, you’ll need to create a “data” folder with four subfolders: “glove”, “bert”, “gpt” and “elmo”. Each one of these folders should have two subfolders: “train” and “test". You can do this manually in a couple minutes, or write a bash script to do it for you. The cleanup.sh script should live in the data folder and clean out (e.g. rm *) everything from each of these folders. 

When you run the full_probes.sh script, you need to supply an argument that’s the name of the folder you keep the comma-separated value files containing the training and testing sentences along with positive and negative labels. 

## Folders
*targeted_tasks*: This folder holds BERT, ELMo, GPT and GLoVe encoders, along with code for constructing the input to these encoders.

*classifiers*: The neural network learners are stored here. _pytorch_classifier.py_ is the main file of interest and has code for a single-layer neural network classifier and a three-layer neural network classifier. Both classifiers are simple multi-layer perceptron (MLP) architectures to increase the interpretability of results and decrease the chance of overfitting.

*results*: Holds .csv files with the results of the probing tasks. The files are in tidy data format: each line has the name of the encoder, the architecture (i.e. size) of the classifier network, the index of the word in our five-word sentences for which the contextualized embedding was constructed, and the performance on the test set.

*data*: The version of this folder on the repository holds the final versions of the stimuli we use as input to the encoders in our experiments. Running _data-construction.py_ writes data to this folder. This "data" is the input to the encoders.

*stimuli*: Contains the ingredients for the data: the nouns and verbs annotated with positive and negative labels for each of the targeted tasks. _data-construction.py_ uses these ingredients to make the input to the encoders.

*word_content*: Holds the encoders for the word identity probing tasks.
