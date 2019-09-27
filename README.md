# effective-probes
This is the home repository for all files related to Josef Klafka and Allyson Ettinger's probing task project. Data is constructed locally and uploaded to the Toyota Technological Institute of Chicago's Slurm computing cluster, where the embedders and classifiers are run on GPU.

## Folders
*classifiers*: The classifiers are stored here. _pytorch_classifier.py_ is the main file of interest and has code for a single layer PyTorch classifier and a three-layer PyTorch classifier.

*results*: Holds .csv files with the results of the probing tasks. The files are in tidy data format: each line has the name of the embedder, the architecture (i.e. size) of the classifier network, the index of the word in our five-word sentences for which the contextualized embedding was constructed, and the performance on the test set.

*data*: Empty folder on the repo. Running _data-construction.py_ writes data to this folder. This "data" is the input to the embedders.

*stimuli*: Contains the ingredients for the data. _data-construction.py_ uses these ingredients to make the input to the embedders.

*word_content*: Holds files related to the word content probing tasks. 
