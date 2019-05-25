#!/bin/bash
. .env/bin/activate
echo Enter the path where Sara exists \(whrite folder name without \'\/\'\) .
read newPATH

python3 $newPATH/installation/BasicAnswers.py

# welcome
mpg123 $newPATH/Voices/introduction.mp3
rm $newPATH/Voices/introduction.mp3
~/Sara.sh
