#!/bin/bash
echo Enter the path where Sara exists \(whrite folder name without \'\/\'\) .
read newPATH
# welcome
mpg123 $newPATH/Voices/introduction.mp3
rm $newPATH/Voices/introduction.mp3
~/Sara.sh
