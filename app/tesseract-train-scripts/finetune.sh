#!/bin/bash

rm -rf output/*
OMP_THREAD_LIMIT=8 lstmtraining \
	--continue_from eng.lstm \
	--model_output output/pubg \
	--traineddata $TESSDATA_PREFIX/eng.traineddata \
	--train_listfile train/eng.training_files.txt \
	--max_iterations 400