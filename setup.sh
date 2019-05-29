#!/bin/bash
# make python and venv
sudo apt-get install python3.7
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
sudo apt-get install python3-venv
sudo apt-get update
python3 -m venv --without-pip .env
. .env/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python3
# apt requirements
sudo apt-get install mpg123
sudo apt-get install portaudio19-dev
sudo apt-get install python3.7-dev
sudo apt-get update
sudo apt-get install python3.7-dev
sudo apt-get update
# pip3 requirements
pip3 install pyaudio
pip3 install -r ./installation/Requirements.txt
# make shortcut
echo Enter the path where Sara exists \(whrite folder name without \'\/\'\) .
read newPATH
sed "s,{__PATH__},${newPATH},g" ./installation/Sara.sh > ~/Sara.sh
chmod +x ~/Sara.sh
cp ./installation/.sara_at_begin.sh ~/
chmod +x ~/.sara_at_begin.sh
# recovery voices
python3 $newPATH/installation/BasicAnswers.py
python3 $newPATH/installation/RepairCommands.py
# welcome
mpg123 $newPATH/Voices/introduction.mp3
rm $newPATH/Voices/introduction.mp3
# massage
echo If you want sara to run automaticly when you start using ubuntu, run ~/.sara_at_begin at your .bashrc script.
# first run
~/Sara.sh
