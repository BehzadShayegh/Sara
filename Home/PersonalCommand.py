import os
import csv
from Home.Listener import Ear
from Home.Writer import HandWriting
from Home.Announcer import Lips

ear = Ear()
handwriting = HandWriting()
lips = Lips()

CommandLabelsPath = './Memorry/CommandLabels.csv'
PersonalCommandsPath = './Memorry/PersonalCommands.csv'
Commands = {}
with open(PersonalCommandsPath, mode='r') as CommandsCsv:
    reader = csv.reader(CommandsCsv)
    Commands = {rows[0]:rows[1] for rows in reader}

def addCommand(possibleCommands) :
    lips.say(lips.writeLinuxCom)
    bashCommand = input()
    lips.say(lips.writeEnLabel)
    label = input()
    lips.say(lips.writePesianKey)
    key = input()
    lastPart = input()

    with open(PersonalCommandsPath, 'a') as CommandsCsv:
        CommandsCsv.write("%s,%s\n"%(label,bashCommand))
    Commands[label] = bashCommand

    with open(CommandLabelsPath, 'a') as CommandLabelsCsv:
        CommandLabelsCsv.write("%s,%s,%s\n"%(label,key,lastPart))
    possibleCommands.append([label,key,lastPart])
    

def personalCommand(command) :
    os.system(Commands[command])