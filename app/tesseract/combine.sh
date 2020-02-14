#!/bin/bash

# Mergin pubg_checkpoint with eng.trainedddata
# pubg_checkpoint is the best model we get
lang="lav"
checkpoint="hypermarket_checkpoint"

lstmtraining \
	--stop_training \
	--continue_from model_output/$checkpoint \
	--traineddata $TESSDATA_PREFIX/$lang.traineddata \
	--model_output model_output/lav.traineddata