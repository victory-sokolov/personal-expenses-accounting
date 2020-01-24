#!/bin/bash

START=$(date +%s)

rm -rf train_data/*
tesstrain.sh --fonts_dir ../../fonts/ \
            --fontlist 'HypermarketW00-Light Light' \
            --lang lav \
            --linedata_only \
            --langdata_dir $TESSDATA_PREFIX/langdata_lstm \
            --tessdata_dir $TESSDATA_PREFIX \
            --save_box_tiff \
            --maxpages 300 \
            --output_dir train_data

END=$(date +%s)
DIFF=$(( $END - $START ))

echo "Execution time: $DIFF seconds"