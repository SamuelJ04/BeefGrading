#!/bin/bash
# basically removes the character at the beginning and then removes the character at the end
# to be able to match to the excel sheet
echo ""
echo "removing 0000 at the beginning"
sleep 1
rename -n 's/^0000|c//' *.jpg
rename 's/^0000|c//' *.jpg
echo ""
echo "removing c at end to match dataset"
sleep 1
rename -n 's/(.*)c(\.[^.]+)$/$1$2/' *
rename 's/(.*)c(\.[^.]+)$/$1$2/' *
echo ""
echo "Renaming done!"
