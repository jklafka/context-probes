cd data
sh cleanup.sh
cd ../embedders
python3 bert_embedder.py $1/train.csv $1/test.csv
python3 elmo_embedder.py $1/train.csv $1/test.csv
python3 gpt_embedder.py $1/train.csv $1/test.csv
python3 glove_embedder.py $1/train.csv $1/test.csv
cd ..
python3 pytorch_classifier.py $1
