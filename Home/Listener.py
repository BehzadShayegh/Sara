import speech_recognition as sr
import re
from Home.Writer import HandWriting
from Home.Announcer import Lips

truefalseAnswers = [['yes','آره','ره'], ['yes','بله','له'], ['no','نه','ن'], ['no','خیر','یر']]
password = ['۰', '۵'] # Sara's bithday is 2019/05/15, so password is ۰ and ۵ in one statement

handwriting = HandWriting()
lips = Lips()

class Ear :
    def __init__(self) :
        pass

    def getWord(self, language, readyFlag=True, timeout=10, phrase_time_limit=3) :
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try :
                if readyFlag : lips.ready_()
                audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                if readyFlag : lips.capture_()
                text = r.recognize_google(audio, language= language)
                if text :
                    handwriting.clientSaid(text)
                    return text
                else :
                    lips.say(lips.didntHear)
                    return None
            except :
                handwriting.wating()

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
        lips.say("Do you mean "+command+"?")
        answer = self.commandListener(truefalseAnswers, 'fa-IR', nearest=False)
        if answer == 'yes' :
            return command
        else :
            lips.ok_()
            return None

    def commandListener(self, commandsList, language, nearest=True, readyFlag=True) :
        text = self.getWord(language, readyFlag=readyFlag)
        if not text : return None
        for commandFlag, command, commandLastPart in commandsList :
            if self.find(command, commandLastPart, text) :
                return commandFlag
        return self.nearest(commandsList, text) if nearest else None

    def checkPassword(self) :
        lips.say(lips.getPass)
        text = self.getWord('fa-IR', readyFlag=True)
        if not text : return False
        for char in password :
            if not (char in text) :
                return False
        return True
