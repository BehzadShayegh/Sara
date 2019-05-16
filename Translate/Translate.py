from gtts import gTTS
import os
from Home.Listener import Listener
from translate import Translator

translator = Translator(from_lang="fa-IR", to_lang="en")
ear = Listener()
possibleCommands = [\
    ['finish', 'پایان', 'یان'],\
    ['finish', 'هیچی', 'چی'],\
    ['finish', 'کافی', 'فیه'],\
    ['finish', 'بس است', 'بسه'],\
    ['finish', 'بی خیال', 'خیال'],\
    ]

def translateToEn() :
    while True :
        os.system("mpg123 ./BasicAnswers/SayTheWordSir.mp3")
        text = ear.getWord("fa-IR", phrase_time_limit=6)
        if not text : continue
        if ear.commandReader(possibleCommands, text, nearest=False) == 'finish' :
            os.system("mpg123 ./BasicAnswers/OkaySir.mp3")
            return
        en_text = translator.translate(text)
        print(en_text) #-------------------------------------
        tts = gTTS(text=en_text, lang='en')
        tts.save("last_word.mp3")
        os.system("mpg123 last_word.mp3")