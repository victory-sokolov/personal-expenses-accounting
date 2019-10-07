function wrap {
    for i in `seq 0 $1`; do
        echo "$2$i$3"
    done
}

N=1 # Change this accordingly to number of files, that you want to feed to tesseract or export it as a script parameter.

# Uncomment this line if, you're rerunning the script
#rm pol.pffmtable  pol.shapetable pol.traineddata pol.unicharset unicharset font_properties pol.inttemp pol.normproto *.tr *.txt

for i in `seq 0 $N`; do
    tesseract lav.MerchantCopy.img.png lav.MerchantCopy.img nobatch box.train
done
unicharset_extractor `wrap $N "lav.merchantcopy.exp" ".box"`
echo "merchantcopy 0 0 0 1 0" > font_properties # tell Tesseract informations about the font
mftraining -F font_properties -U unicharset -O lav.unicharset `wrap $N "lav.merchantcopy.exp" ".tr"`
cntraining `wrap $N "lav.merchantcopy.exp" ".tr"`
# rename all files created by mftraing en cntraining, add the prefix lav.:
mv inttemp lav.inttemp
mv normproto lav.normproto
mv pffmtable lav.pffmtable
mv shapetable lav.shapetable
combine_tessdata lav.
