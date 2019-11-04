#!/bin/bash
#SBATCH --job-name=torch_probes
#SBATCH --error=full_probes.err
#SBATCH --output=full_probes.out
#SBATCH --mail-user=jklafka@andrew.cmu.edu
#SBATCH --mail-type=END,FAIL

declare -a tasks=("subject_number" "subject_gender" "subject_animacy"
                  "object_number" "object_gender" "object_animacy"
                  "verb_tense" "verb_dynamic" "verb_causative")

for i in "${tasks[@]}"
  do
    sh probe_task.sh "$i"
  done
