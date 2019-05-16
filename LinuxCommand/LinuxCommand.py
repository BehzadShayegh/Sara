from gtts import gTTS
import os
from Home.Listener import Listener
import csv

ear = Listener()

CommandLabels = './LinuxCommand/CommandLabels.csv'
possibleCommands = []
with open(CommandLabels, 'r') as CommandLabelsCsv:
    readedFile = csv.reader(CommandLabelsCsv, delimiter=',')
    firstRow = True
    for row in readedFile :
        if firstRow :
            firstRow = False
            continue
        possibleCommands.append(row)

Commands = './LinuxCommand/Commands.csv'
linuxCommands = {}
with open(Commands, mode='r') as CommandsCsv:
    reader = csv.reader(CommandsCsv)
    linuxCommands = {rows[0]:rows[1] for rows in reader}

def addCommand() :
    tts = gTTS(text='write your linux bash command', lang='en')
    tts.save("last_word.mp3")
    os.system("mpg123 last_word.mp3")
    bashCommand = input()

    tts = gTTS(text='write a english label for that', lang='en')
    tts.save("last_word.mp3")
    os.system("mpg123 last_word.mp3")
    label = input()

    tts = gTTS(text='write your persian key word \
        and last part of that in new line after that', lang='en')
    tts.save("last_word.mp3")
    os.system("mpg123 last_word.mp3")
    key = input()
    lastPart = input()

    with open(Commands, 'a') as CommandsCsv:
        CommandsCsv.write("%s,%s\n"%(label,bashCommand))
    linuxCommands[label] = bashCommand

    with open(CommandLabels, 'a') as CommandLabelsCsv:
        CommandLabelsCsv.write("%s,%s,%s\n"%(label,key,lastPart))
    possibleCommands.append([label,key,lastPart])
    
    os.system("mpg123 ./BasicAnswers/JobDoneSir.mp3")

def linuxCommand() :
    while True :
        os.system("mpg123 ./BasicAnswers/TellMeWhatYouWant.mp3")
        command = ear.commandListener(possibleCommands, 'fa-IR')
        if command == 'finish' :
            os.system("mpg123 ./BasicAnswers/OkaySir.mp3")
            break
        elif command == 'add' :
            addCommand()
            continue
        elif command == 'remove' :
            # removeCommand()
            continue
        elif command in linuxCommands :
            os.system(linuxCommands[command])
            os.system("mpg123 ./BasicAnswers/JobDoneSir.mp3")
            continue
        else :
            os.system("mpg123 ./BasicAnswers/ICanNotUnderstandSir.mp3")