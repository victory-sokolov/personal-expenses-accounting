#!/bin/bash

# default model --model lav.lstm

lstmeval \
  --model ../tesseract/model_output/hypermarket_checkpoint \
  --traineddata ../tesseract/model_output/lav.traineddata \
  --eval_listfile ../tesseract/train_data/lav.training_files.txt
