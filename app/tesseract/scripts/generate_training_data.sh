#!/bin/bash

START=$(date +%s)

lang="lav"
pages=5

rm -rf train_data/*
tesstrain.sh \
            --fonts_dir ../../../fonts \
            --fontlist 'OCR-A' \
            --lang $lang \
            --noextract_font_properties \
            --linedata_only \
            --langdata_dir $TESSDATA_PREFIX/langdata_lstm \
            --tessdata_dir $TESSDATA_PREFIX \
            --save_box_tiff \
            --maxpages $pages \
            --output_dir train_data

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "Execution time: $DIFF seconds"
