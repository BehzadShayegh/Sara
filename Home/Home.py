import os
from Home.Listener import Listener
from Translate.Translate import translateToEn
from LinuxCommand.LinuxCommand import linuxCommand
import pyjokes

ear = Listener()
possibleCommands = [\
    ['linuxCommand', 'دستور', 'تور'],\
    ['finish', 'پایان', 'یان'],\
    ['finish', 'هیچی', 'چی'],\
    ['finish', 'کافی', 'فیه'],\
    ['finish', 'بس است', 'بسه'],\
    ['finish', 'بی خیال', 'خیال'],\
    ['translate', 'ترجمه', 'جمه'],\
    ['shutdown', 'لپتاپ', 'تاپ'],\
    ['shutdown', 'خاموش', 'موش'],\
    ['joke', 'جوک', 'جوک'],\
    ['joke', 'لطیفه', 'تیف'],\
    ]

from gtts import gTTS
def learnNewCommand() :
    try :
        tts = gTTS(text='I can not learn any thing to day. sorry sir!', lang='en-US')
        tts.save("last_word.mp3")
        os.system("mpg123 last_word.mp3")
    except :
        os.system("mpg123 ./BasicAnswers/ICanNotUnderstandSir.mp3")

def listenToCommand() :
    while True :
        command = ear.commandListener(possibleCommands, 'fa-IR')
        if command == 'finish' :
            os.system("mpg123 ./BasicAnswers/OkaySir.mp3")
            break
        elif command == 'translate' :
            translateToEn()
            break
        elif command == 'linuxCommand' :
            linuxCommand()
            break
        elif command == 'shutdown' :
            if ear.checkPassword() :
                os.system("mpg123 ./BasicAnswers/ShutDown.mp3")
                os.system("shutdown now")
            else :
                os.system("mpg123 ./BasicAnswers/OkaySir.mp3")
        elif command == 'joke' :
            text = pyjokes.get_joke()
            tts = gTTS(text=text, lang='en-US')
            tts.save("last_word.mp3")
            os.system("mpg123 last_word.mp3")
            print("\n\n\n:DD :DD :DD :DD :DD :DD :DD :DD :DD")
            print(text)
            print(":DD :DD :DD :DD :DD :DD :DD :DD :DD\n\n\n")
        else :
            os.system("mpg123 ./BasicAnswers/ICanNotUnderstandSir.mp3")
