#!/bin/bash


# Base evaluation model
# lstmeval --model eng.lstm \
#   --traineddata tesseract/tessdata/eng.traineddata \
#   --eval_listfile train/eng.training_files.txt


lstmeval --model output/pubg_checkpoint \
  --traineddata $TESSDATA_PREFIX/eng.traineddata \
  --eval_listfile train/eng.training_files.txt