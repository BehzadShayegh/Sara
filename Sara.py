import os
from Home.Listener import Ear
from Home.Home import listenToCommand
from Home.Announcer import Lips

ear = Ear()
lips = Lips()
possibleCommands = [\
    ['sara', 'سارا', 'ارا'],\
    ['off', 'خاموش', 'موش'],\
    ]

lips.say(lips.welcome)
while True :
    command = ear.commandListener(possibleCommands, 'fa-IR', nearest=False, readyFlag=False)
    if command == 'off' :
        lips.goodbye_()
        break
    elif command == 'sara' :
        lips.yes_()
        listenToCommand()