import os
from Home.Listener import Listener
from Home.Home import listenToCommand

ear = Listener()
possibleCommands = [\
    ['sara', 'سارا', 'ارا'],\
    ['off', 'خاموش', 'موش'],\
    ]

os.system("mpg123 ./Voices/WelcomeYourHighness.mp3")
while True :
    command = ear.commandListener(possibleCommands, 'fa-IR', nearest=False, readyFlag=False)
    if command == 'off' :
        os.system("mpg123 ./Voices/GoodByeMr.mp3")
        break
    elif command == 'sara' :
        os.system("mpg123 ./Voices/YesSir.mp3")
        listenToCommand()