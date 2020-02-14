#!/bin/bash

START=$(date +%s)

lang="lav"

rm -rf train_data/*
tesstrain.sh \
            --fonts_dir ../../fonts \
            --fontlist 'HypermarketW00-Light Light' \
            --lang $lang \
            --noextract_font_properties \
            --linedata_only \
            --langdata_dir $TESSDATA_PREFIX/langdata_lstm \
            --tessdata_dir $TESSDATA_PREFIX \
            --save_box_tiff \
            --maxpages 20 \
            --output_dir train_data

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "Execution time: $DIFF seconds"