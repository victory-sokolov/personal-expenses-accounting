#!/bin/bash

lang="lav"

lstmtraining \
	--continue_from $lang.lstm \
	--model_output model_output/hypermarket \
	--traineddata $TESSDATA_PREFIX/$lang.traineddata \
	--train_listfile train_data/$lang.training_files.txt \
	--max_iterations 400
	#&> train.log