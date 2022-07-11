#!/usr/bin/env bash

# Test gpu
nvidia-smi

# Handle new users (allows non root runners to work - I think)
conda init bash
. ~/.bashrc

# Activate our environment
conda activate $WRK/env

# Run - note, there is a dependence that the target python file be available on the path somewhere
# So it is best to map a local dir to your docker dir
python /data/$1