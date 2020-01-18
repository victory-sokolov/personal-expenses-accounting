#!/bin/bash

# Mergin pubg_checkpoint with eng.trainedddata
# pubg_checkpoint is the best model we get

lstmtraining --stop_training \
	--continue_from output/pubg_checkpoint \
	--traineddata $TESSDATA_PREFIX/tessdata/eng.traineddata \
	--model_output output/pubg.traineddata