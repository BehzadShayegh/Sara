import os
import csv
from Home.Listener import Listener
from Home.PersonalCommand import personalCommand, addCommand
from Home.Joker import tellJoke

ear = Listener()

CommandLabels = './Memorry/CommandLabels.csv'
possibleCommands = []
with open(CommandLabels, 'r') as CommandLabelsCsv:
    readedFile = csv.reader(CommandLabelsCsv, delimiter=',')
    firstRow = True
    for row in readedFile :
        if firstRow :
            firstRow = False
            continue
        possibleCommands.append(row)

def listenToCommand() :
    while True :
        command = ear.commandListener(possibleCommands, 'fa-IR')

        if not command :
            os.system("mpg123 ./Voices/ICanNotUnderstandSir.mp3")
            continue

        elif command == 'sara' :
            os.system("mpg123 ./Voices/ImListeningSir.mp3")
            continue

        elif command == 'finish' :
            os.system("mpg123 ./Voices/OkaySir.mp3")
            break

        elif command == 'shutdown' :
            if ear.checkPassword() :
                os.system("mpg123 ./Voices/ShutDown.mp3")
                os.system("shutdown now")
            else :
                os.system("mpg123 ./Voices/OkaySir.mp3")

        elif command == 'joke' :
            tellJoke()
            continue

        elif command == 'add command' :
            addCommand(possibleCommands)
            os.system("mpg123 ./Voices/JobDoneSir.mp3")
            continue

        elif command == 'remove command' :
            # removeCommand()
            continue

        else :
            personalCommand(command)
            os.system("mpg123 ./Voices/JobDoneSir.mp3")
            continue