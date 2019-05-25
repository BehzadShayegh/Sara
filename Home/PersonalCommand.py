import os
import csv
from Home.Listener import Listener

ear = Listener()

CommandLabelsPath = './Memorry/CommandLabels.csv'
PersonalCommandsPath = './Memorry/PersonalCommands.csv'
Commands = {}
with open(PersonalCommandsPath, mode='r') as CommandsCsv:
    reader = csv.reader(CommandsCsv)
    Commands = {rows[0]:rows[1] for rows in reader}

def addCommand(possibleCommands) :
    os.system("mpg123 ./Voices/WriteLinuxBashCommand.mp3")
    bashCommand = input()
    os.system("mpg123 ./Voices/WriteEnglishLabel.mp3")
    label = input()
    os.system("mpg123 ./Voices/WritePersianKeyWord.mp3")
    key = input()
    lastPart = input()

    with open(PersonalCommandsPath, 'a') as CommandsCsv:
        CommandsCsv.write("%s,%s\n"%(label,bashCommand))
    Commands[label] = bashCommand

    with open(CommandLabelsPath, 'a') as CommandLabelsCsv:
        CommandLabelsCsv.write("%s,%s,%s\n"%(label,key,lastPart))
    possibleCommands.append([label,key,lastPart])
    

def personalCommand(command) :
    print(Commands[command])
    os.system(Commands[command])