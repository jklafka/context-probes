#!/bin/bash
#SBATCH --job-name=torch_probes
#SBATCH --error=full_probes.err
#SBATCH --output=full_probes.out
#SBATCH --mail-user=jklafka@andrew.cmu.edu
#SBATCH --mail-type=END,FAIL

cd data
sh cleanup.sh
cd ../embedders
python3 bert_embedder.py $1/train.csv $1/test.csv
python3 elmo_embedder.py $1/train.csv $1/test.csv
python3 gpt_embedder.py $1/train.csv $1/test.csv
python3 glove_embedder.py $1/train.csv $1/test.csv
cd ..
python3 pytorch_classifier.py $1
