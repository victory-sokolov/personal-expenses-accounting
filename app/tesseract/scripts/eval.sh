#!/bin/bash

# default model --model lav.lstm

lstmeval \
  --model model_output/hypermarket_checkpoint \
  --traineddata model_output/lav.traineddata \
  --eval_listfile train_data/lav.training_files.txt
