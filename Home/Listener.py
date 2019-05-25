import speech_recognition as sr
from gtts import gTTS
import os
import re

truefalseAnswers = [['yes','آره','ره'], ['yes','بله','له'], ['no','نه','ن'], ['no','خیر','یر']]
password = ['۰', '۵'] # Sara's bithday is 2019/05/15, so password is ۰ and ۵ in one statement

class Listener :
    def __init__(self) :
        pass

    def getWord(self, language, readyFlag=True, timeout=10, phrase_time_limit=3) :
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try :
                if readyFlag : os.system("mpg123 ./Voices/Ready.mp3")
                audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                if readyFlag : os.system("mpg123 ./Voices/Capture.mp3")
                text = r.recognize_google(audio, language= language)
                if text :
                    print(text)
                    return text
                else :
                    os.system("mpg123 ./Voices/IDidntHearAnyThingSir.mp3")
                    return None
            except :
                print('.')

    def find(self, word, lastPart, text) :
        return len(re.findall('[-\w.]?\\'+lastPart, text) + re.findall('[-\w.]?\\'+word+'?[-\w.]', text)) != 0

    def nearest(self, commandsList, text) :
        length = len(text)
        commandsNumber = len(commandsList)
        points = [0 for i in range(commandsNumber)]
        for searchSize in range(min([5,length])) :
            for start in range(length-searchSize) :
                for index in range(commandsNumber) :
                    if text[start : start+searchSize] in commandsList[index][1] :
                        points[index] += searchSize
        command = commandsList[points.index(max(points))][0]
        tts = gTTS(text="Do you mean "+command+"?", lang='en')
        tts.save("./Voices/last_word.mp3")
        os.system("mpg123 ./Voices/last_word.mp3")
        os.system("rm ./Voices/last_word")
        answer = self.commandListener(truefalseAnswers, 'fa-IR', nearest=False)
        if answer == 'yes' :
            return command
        else :
            os.system("mpg123 ./Voices/OkaySir.mp3")
            return None

    def commandListener(self, commandsList, language, nearest=True, readyFlag=True) :
        text = self.getWord(language, readyFlag=readyFlag)
        if not text : return None
        for commandFlag, command, commandLastPart in commandsList :
            if self.find(command, commandLastPart, text) :
                return commandFlag
        return self.nearest(commandsList, text) if nearest else None

    def checkPassword(self) :
        os.system("mpg123 ./Voices/GetPassword.mp3")
        text = self.getWord('fa-IR', readyFlag=True)
        if not text : return False
        for char in password :
            if not (char in text) :
                return False
        return True
