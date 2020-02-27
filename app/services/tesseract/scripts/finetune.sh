#!/bin/bash

lang="eng"

lstmtraining \
	--continue_from ./$lang.lstm \
	--model_output ./model/ \
	--traineddata $TESSDATA_PREFIX/$lang.traineddata \
	--train_listfile ./training_data/$lang.training_files.txt \
	--max_iterations 400
	#&> train.log