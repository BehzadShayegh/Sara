import os
from pandas import DataFrame, read_csv
import pandas as pd
import pyjokes
from Home.Listener import Ear
from Home.Announcer import Lips
from Home.Writer import HandWriting
from Home.PersonalCommand import personalCommand, addCommand

ear = Ear()
lips = Lips()
handwriting = HandWriting()

CommandLabelsCsv = './Memorry/CommandLabels.csv'
possibleCommands = pd.read_csv(CommandLabelsCsv).values.tolist()

def listenToCommand() :
    while True :
        command = ear.commandListener(possibleCommands, 'fa-IR')
        if command : handwriting.specialLog(command)

        if not command :
            lips.notUnderStand_()
            continue

        elif command == 'sara' :
            lips.say(lips.listenning)
            continue

        elif command == 'finish' :
            lips.ok_()
            break

        elif command == 'shutdown' :
            if ear.checkPassword() :
                lips.say(lips.shutdown)
                os.system("shutdown now")
            else :
                lips.ok_()

        elif command == 'joke' :
            lips.say(pyjokes.get_joke())
            continue

        elif command == 'add command' :
            addCommand(possibleCommands)
            lips.jobDone_()
            continue

        elif command == 'remove command' :
            # removeCommand()
            continue

        else :
            personalCommand(command)
            lips.jobDone_()
            continue